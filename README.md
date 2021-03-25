# User-Management-System. (User interaction)

## Motivation
-User interaction django web application for send and receive text and file information.
-profile dashboard for users.





## Using Project Locally
1. Clone the repository `git clone https://github.com/bpagare6/Portfolio-Management-System.git`
2. Create virtual environment inside the `Portfolio-Management-System` folder.
3. Activate the virtual environment.
4. Download the requirements, `pip install requirements.txt`
5. Go inside the `portfolio_management_system` folder which is actual Django project.
6. Create a .env file from which your environment variables will be fetched.
7. Make database up to date, `python manage.py makemigrations` and `python manage.py migrate`
8. Run the project `python manage.py runserver`
9. Visit `localhost:8000` in your browser and you should be able to use the project :smiley:.

## Project Progress
- [x] Home Page (Content, Images are yet to be updated)
- [x] Login & Register Page (Logo, Footer are yet to be updated)
- [x] Dashboard UI (Logo, Footer are yet to be updated)
- [x] Dashboard (Investment Overview) - Backend Integration
  - [x] Some Utility Functions (Adding Stocks to Holdings, View Details on dashboard)
  - [ ] Solve issues regarding Alphavantage API request limit (using try-except)
  - [ ] Solve issues regarding TradingView glitches
- [ ] Dashboard (Portfolio Insights, Recommendations) - Backend Integration
- [ ] Risk Profile Page and Backend
- [ ] Database Models (Under Progress)
  - [x] Portfolio Model
  - [x] StockHoldings Model




ref:  https://github.com/bpagare6/Portfolio-Management-System
