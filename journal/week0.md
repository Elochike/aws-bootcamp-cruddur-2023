# Week 0 — Billing and Architecture


**Set a Billing alarm [Precorded]**
To monitor our spending by using billing alarms on cloud watch. Cloud watch > alarms > billing, then clicked on create alarm. Namespace:AWS/Billing , Metric name: Estimated Charges, Currency: USD
Then set the conditions threshold to a static value. whenever the estimated charges is greater than the static amount it should give me an alarm. The alarm state trigger “in alarm, then create an SNS topic(MyBillingAlarm) in order to send a message to my email. Then I had to go to my email to respond to the pending confirmation in order to subscribe to it.
 
![BillingAlarm]([bill alarm.png](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/881b8b8573668ac1a78e81fa5ed7c346b78395aa/buget.PNG))


**Set an AWS Budget [Precorded],**
I  created two  budgets one for credits and the other for 
Go to the Billing Console > Budgets > Create a budget – I had to choose a budget type, cost budget (recommended), and my cost budget was set to the period (monthly) reoccurring budget, fixed and I entered my budgeted amount. Then named it on credits and configured an alert by 80% of budgeted amount. I also created a Zerospend buget too
 

