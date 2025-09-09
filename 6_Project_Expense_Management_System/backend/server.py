from fastapi import FastAPI,HTTPException
import db_helper
from typing import List
from pydantic import BaseModel
from datetime import date


class Expense(BaseModel):
    #id:int
    #expense_date : date
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date: date
    end_date: date




app=FastAPI()

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def fetch_expenses_for_expenses_date(expense_date):
    expense=db_helper.fetch_expenses_for_date(expense_date)
    if expense is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense from the database .")
    return expense


@app.post("/expenses/{expense_date}")
def insert_expenses_for_expenses_date(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)

    return {"message": "Expenses inserted successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expenses_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")



    total = sum([row['total']for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            'Total': row['total'],
            'Percentage': percentage
        }
    return breakdown


@app.post("/monthly_summary")
def get_analytics_by_months(date_range: DateRange):
    data = db_helper.fetch_expenses_summary_by_months(date_range.start_date, date_range.end_date)
    return data



