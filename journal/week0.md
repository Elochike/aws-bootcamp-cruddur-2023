# Week 0 — Billing and Architecture

**homework Hard Assignments**
**Set a Billing alarm [Precorded]**
To monitor our spending by using billing alarms on cloud watch. Cloud watch > alarms > billing, then clicked on create alarm. Namespace:AWS/Billing , Metric name: Estimated Charges, Currency: USD
Then set the conditions threshold to a static value. whenever the estimated charges is greater than the static amount it should give me an alarm. The alarm state trigger “in alarm, then create an SNS topic(MyBillingAlarm) in order to send a message to my email. Then I had to go to my email to respond to the pending confirmation in order to subscribe to it.
 
![bill](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/bill-alarm.png.PNG)



**Set an AWS Budget [Precorded],**
I  created two  budgets one for credits and the other for 
Go to the Billing Console > Budgets > Create a budget – I had to choose a budget type, cost budget (recommended), and my cost budget was set to the period (monthly) reoccurring budget, fixed and I entered my budgeted amount. Then named it on credits and configured an alert by 80% of budgeted amount. I also created a Zerospend buget too
 
![buget](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/buget.PNG)


**Generating AWS Credentials [Precorded]**
At IAM > users >Username > create accesskey . and created an  access key



** CloudShell [Precorded]**



**Conceptual Architecture Diagram or your Napkins [Live-Stream]**
 ![conceptualArc](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/conceptua-design.PNG)


**mework  Stretch Assignments**
**Destroy your root account credentials ,set MFA,IAM role**
Creating an AWS account: I created an aws account and signed in to the account as a root user then I had to assign an IAM user using the root user account.
A group was then created in order to assign the new IAM user to the group which had admin privileges.
Then logged in using the new IAM account and set up MFA, by setting up the device going to IAM>Securitycredentials> AssignMFA device, and installing an application on my phone (google authenticator) which would be used to scan the QR codes. For generating numbers for authentication

 
Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue.

Review all the questions of each pillars in the Well Architected Tool (No specialized lens)

Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts

Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility. 

Open a support ticket and request a service limit

