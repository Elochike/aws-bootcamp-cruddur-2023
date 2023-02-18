# Week 0 — Billing and Architecture

**Homework Assignments**

**Generating credentials ,set MFA,IAM role**

- Create an aws account and signed in to the account as a root user.
- Then assign an IAM user using the root user account.
- A group was then created in order to assign the new IAM user to the group which had admin privileges.
- Then logged in using the new IAM account and set up MFA.
- To set up the device go to IAM > Securitycredentials > AssignMFA device, and installing an application on my phone (google authenticator) which would be used to scan the QR codes.
- To generate access keys go to access keys and click create acces keys

![IAM](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/summary.PNG)

**Set a Billing alarm**

- To monitor our spending by using billing alarms on cloud watch.
- Search for Cloud watch > alarms > billing, then clicked on create alarm. 
- Namespace:AWS/Billing , Metric name: Estimated Charges, Currency: USD
- Then set the conditions threshold to a static value.
- whenever the estimated charges is greater than the static amount it should give you an alarm. 
- he alarm state trigger “in alarm, then create an SNS topic(MyBillingAlarm) in order to send a message to my email.
- Then go to you email to respond to the pending confirmation in order to subscribe to it.
 
![bill](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/bill-alarm.png.PNG)

**Set an AWS Budget**

- Go to the Billing Console > Budgets > Create a budget 
– Choose a budget type, cost budget (recommended), 
- cost budget was set to the period (monthly) reoccurring budget, fixed and enter budgeted amount. 
- Then named it one credits and configured an alert by 80% of budgeted amount.
- Created a Zerospend buget too
 
![buget](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/buget.PNG)

**Setting up AWS Organization Unit**

- Having to manage multiple accounts is of importance and aws organization unit helps with that. 
- log into your root account as thats youer management account and it is advised to great accounts under root account for security concerns. 
- Once you **chech the root** box you can click on **actions** > **create new** you could add **Tags** which helps you to identify what they are.
- You can also decide to add Security control policies to your orcanisation unit. 
- On the menu side bar click on polices then click on security polices. 
- Then create and attach the policy to an organization unit.

![OrganizationUnit](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/OU.PNG)

**Enabiling cloud trail**
- AWS cloud trail is of importance when it comes to security.
- This helps to trace all activites/API call made on your aWS account . 
- It takes record of logs and stores it in an S3 bucket. 
- This log can then be view for audits and incident responce purposes. 
- On the **search bar** write **cloud trail** then click on **create trail** . 
- You coould enable for all account in my organisation and the click on an S3 bucket for storage if you have one . 
- Enter KMS alias and tags are optional.

![Cloudtrail](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/cloud%20trail.PNG)

**CloudShell**
- Cloud shell (AWS CLI) a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. But we would need to install clous shell into our workspace so as to contol it from there. 
- Youll need the access key details to login into our clous shell(AWS CLI) through **gitpod**(workspace).
- Login into gitpod and connect you github account and open the repository.
- Download the AWS CLI with the curl command and Unzip the file with unzip awscliv2.zip

![donwloadAWS](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/o;hiohi.PNG)

- Then insall AWS CLI with the SuperUserDo commmand,and run aws --version to check its installed. 
- The next tep is to put in your access ke credentials and save it by usin **gp env**. 
- Then use aws sts get-caller-identity for user info.

![accesskey](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/jgipho.PNG)

- For Gitpod , you may come back to the workspace and there may be a new instance spun up. 
- in other to perform the previous task you need to write out a yaml code. 
- Then close gitpod and sin up a new workspace to test.

![gitpodcodw](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/gitpodcode.PNG)


**Conceptual Architecture Diagram or your Napkins**

![Napkindesign](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/bbeb1fbc-8b05-4a32-a3cd-76130facdb6d.jpg)

![conceptualArc](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/conceptua-design.PNG)
https://lucid.app/lucidchart/f2bc0e89-f376-4a2e-99af-84f7dbf4cbe4/edit?viewport_loc=-571%2C89%2C1961%2C1185%2C0_0&invitationId=inv_9eb74dfe-ab25-4695-b4ff-ad8dd855642f

![logical](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/logical%20design.PNG)

https://lucid.app/lucidchart/ed511b9c-37e6-4020-8ea5-e820ab61a519/edit?viewport_loc=-572%2C-154%2C2807%2C1696%2C0_0&invitationId=inv_959cd19b-23a5-4392-b464-4b67d8ee6e7b


**Homework  Challenges**

**Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts**

![CI/CD](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/cicd.PNG)
https://lucid.app/lucidchart/14e84ae5-0f20-4768-904f-f305e3b4439f/edit?viewport_loc=-814%2C996%2C3837%2C2318%2C0_0&invitationId=inv_ebcecd02-b35c-48dd-8bf0-4a4a406d79e6

