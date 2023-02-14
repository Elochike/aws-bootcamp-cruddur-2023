# Week 0 — Billing and Architecture

**Homework Assignments**

**Set a Billing alarm**

To monitor our spending by using billing alarms on cloud watch. Cloud watch > alarms > billing, then clicked on create alarm. Namespace:AWS/Billing , Metric name: Estimated Charges, Currency: USD
Then set the conditions threshold to a static value. whenever the estimated charges is greater than the static amount it should give me an alarm. The alarm state trigger “in alarm, then create an SNS topic(MyBillingAlarm) in order to send a message to my email. Then I had to go to my email to respond to the pending confirmation in order to subscribe to it.
 
![bill](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/bill-alarm.png.PNG)

**Set an AWS Budget**

I  created two  budgets one for credits and the other for 
Go to the Billing Console > Budgets > Create a budget – I had to choose a budget type, cost budget (recommended), and my cost budget was set to the period (monthly) reoccurring budget, fixed and I entered my budgeted amount. Then named it on credits and configured an alert by 80% of budgeted amount. I also created a Zerospend buget too
 
![buget](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/buget.PNG)

**Setting up AWS Organization Unit**
Having to manage multiple accounts is of importance and aws organization unit helps with that. You need to log into your root account as thats youer management account and it is advised to great accounts under root account for security concerns. Once you **chech the root** box you can click on **actions** > **create new** you could add **Tags** which helps you to identify what they are. You can also decide to add Security control policies to your orcanisation unit. On the menu side bar click on polices then click on security polices. Then you could create and attach the policy to an organization unit.


**Generating AWS Credentials**

At IAM > users >Username > create accesskey . and created an  access key


**CloudShell**

**Conceptual Architecture Diagram or your Napkins**

![Napkindesign](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/bbeb1fbc-8b05-4a32-a3cd-76130facdb6d.jpg)

 ![conceptualArc](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/conceptua-design.PNG)
https://lucid.app/lucidchart/f2bc0e89-f376-4a2e-99af-84f7dbf4cbe4/edit?viewport_loc=-571%2C89%2C1961%2C1185%2C0_0&invitationId=inv_9eb74dfe-ab25-4695-b4ff-ad8dd855642f

**Homework  Challenges**

**Destroy your root account credentials ,set MFA,IAM role**

Creating an AWS account: I created an aws account and signed in to the account as a root user then I had to assign an IAM user using the root user account.
A group was then created in order to assign the new IAM user to the group which had admin privileges.
Then logged in using the new IAM account and set up MFA, by setting up the device going to IAM>Securitycredentials> AssignMFA device, and installing an application on my phone (google authenticator) which would be used to scan the QR codes. For generating numbers for authentication.

![IAM](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/summary.PNG)
 
Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue.

Review all the questions of each pillars in the Well Architected Tool (No specialized lens)

Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts

![logical](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/logical%20design.PNG)

https://lucid.app/lucidchart/ed511b9c-37e6-4020-8ea5-e820ab61a519/edit?viewport_loc=-572%2C-154%2C2807%2C1696%2C0_0&invitationId=inv_959cd19b-23a5-4392-b464-4b67d8ee6e7b

Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility. 

Open a support ticket and request a service limit

