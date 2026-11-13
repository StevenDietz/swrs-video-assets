# SWRS portal how-to videos: build kit (2026-11-12)

Pipeline: Firecrawl portal help pages + Vimeo training videos (transcribed with ElevenLabs Scribe, see PORTAL-VIDEO-TRANSCRIPTS.md) -> narration scripts below -> ElevenLabs TTS (voice Bella, eleven_multilingual_v2, stability 0.7, similarity 0.75, speed 0.96) -> Playwright slides 1920x1080 with sanitized portal screenshots -> ffmpeg per-scene clips, loudnorm -16 LUFS -> concat per video -> verify by transcribing the final audio and diffing against the script. Keys are read from attached files; none are stored here.

Corrections applied (Steven): portal passwords are NOT case-sensitive (the login help page and login video still say they are). Support contact is 866-837-3065 / info@swrecovery.com only; (214) 387-8068 appears in the login and vault videos and is not used.

Video page: https://claude.ai/artifact/NqPvmEwGHx4GyAWNE2aFwM (private until shared). Links: #login #reset-password #profile-mfa #reports #debtor-status #debtor-history #upload-files #new-placements #update-account #document-vault #direct-payment

## Narration scripts (v3, from transcripts)

### login: How to log in (1:31)
1. [Sign in] To access the Southwest Recovery Services client portal, open your browser and go to S W R S portal dot com. On the login screen, enter the username assigned to your portal account, then enter your password. When you're ready, click Login. You'll be taken directly to your dashboard.
2. [First time, forgot it, or locked out?] If this is your first time logging in and you haven't received your initial credentials, reach out to your account manager, and they'll get you set up. If you've forgotten your password, click Forgot password. We have a separate short video for that. If your account becomes locked after multiple failed login attempts, contact the S W R S support team to have it unlocked. Use the phone number or email at the end of this video.
3. [Two portal roles] Your access depends on your role. Standard users can view activity reports, look up debtor status, upload files, report direct payments, and use the Secure Document Vault. Managers can do all of that, plus switch between client accounts and run consolidated manager reports. To add a user or change a role, email info at S W recovery dot com with the person's name, email address, and the role you need.

### reset-password: How to reset your password (2:18)
1. [Start the reset] If you've forgotten your password, click the Forgot Password link on the login page. This opens the reset request form. The reset has two confirmation steps, and takes about two minutes.
2. [Request the reset] Enter the email address registered to your portal account, and click Send Confirmation Email. If an account exists for that address, you'll receive the first email in the reset sequence within a few minutes.
3. [Confirm the request] Check your inbox for a message from Portal S at S W recovery dot com, with the subject line, Confirm Your Password Reset Request. Open that email, and click the Confirm Password Reset link. This verifies that you made the request, and opens a confirmation page in your browser. If you didn't request a reset, simply ignore the email. Your password won't be changed.
4. [Confirm on the portal] On that confirmation page, click the Confirm Password Reset button to complete the verification step. The portal will then send you a second email with your actual reset link.
5. [Open the reset link] After you confirm on the portal page, a second email will arrive with the subject line, Reset your password. Open that email, and click the Reset Password link. This takes you to the New Password form. Complete this step promptly. The link expires shortly after it's sent.
6. [Set your new password] On the form, enter your new password. It must be at least eight characters. Re-enter it in the confirm field, then click Set New Password. That's it. You can now log in at S W R S portal dot com with your new password.
7. [If something goes wrong] One helpful tip. If either email doesn't show up within a few minutes, check your spam or junk folder. Both emails come from Portal S at S W recovery dot com, so adding that address to your safe senders list will prevent future filtering. If nothing arrives after five minutes, start the reset again, or contact support. If a link has expired, start over from the login page.

### profile-mfa: My Profile and MFA (2:25)
1. [Open My Profile] The My Profile page is where you manage your personal portal settings. To access it, click My Profile in the left sidebar of your dashboard. At the top, you'll see your username and email address. These are the credentials registered to your portal account. If either needs to be updated, reach out to your account manager. Below that are two sections: Multi-Factor Authentication, which lets you enable or disable email verification for your logins, and Change Password, which lets you update your portal password at any time. The Back to Home link returns you to your dashboard without making any changes.
2. [Turn on MFA] Multi-Factor Authentication, or M F A, adds a second layer of security to your login. When enabled, you'll receive a six-digit verification code by email each time you sign in. We strongly recommend enabling it on all portal accounts. To get started, check the Enable M F A checkbox on the My Profile page. The setup panel will expand, showing the email address where your codes will be sent. Click Send Code.
3. [Check your email] You'll be taken to the verification page, and a six-digit code will arrive in your inbox from Portal S at S W recovery dot com. Don't share the code with anyone. The code expires in ten minutes, so enter it promptly.
4. [Verify your login] Enter that code, and click Verify. If it expires before you get to it, just click Resend Code to get a fresh one. Each new code replaces the one before it.
5. [MFA is active] Once verified, you'll be returned to My Profile, and a green confirmation panel will show that M F A is now active on your account. To turn M F A off, uncheck the box. It turns off immediately.
6. [Change your password] To change your password, scroll to the Change Password section. Enter your current password, then your new password twice. It must be at least eight characters. Click Change Password, and it takes effect immediately. If you've forgotten your current password, use Forgot password on the login page instead.

### reports: How to run an activity report (2:55)
1. [Open the report] The Debtor Activity Report lets you view all notes and actions recorded against your accounts for any date range you choose. To get started, click View Activity Report in the left sidebar of your portal dashboard. This opens the filter dialog. You have two ways to set your date range. The quick select buttons, This Week, This Month, and This Year, automatically fill in the From and To fields for you. Or if you need a specific window, enter your own custom From and To dates. The report supports ranges up to three hundred sixty-six days, and will prompt you to confirm anything longer than a year.
2. [Filter by debtor (optional)] You can also narrow your results to a specific debtor. Set the Search By field to Last Name, First Name, or Account Number. Then type a value in the Contains field. If you want to see your full portfolio, leave both fields blank. When you're ready, click View Report. Your results will load in the same window.
3. [Read the results] Once your report loads, you'll see every recorded note and action for your accounts within the selected date range, sorted alphabetically by debtor last name. The report header shows the date range the report was run for, along with a back link, so you can return to the filter dialog. Each row is a single activity record. It shows the debtor name, account number, the date and time of the activity, and a note describing what happened, such as an email sent, a workflow triggered, or a payment posted. Some debtors appear more than once, and that's completely normal. One row is the direct email sent to the debtor, and another is the automated workflow it triggered. Both are captured for audit purposes.
4. [Export to CSV] To export your report, click the Download C S V button in the top right corner of the results page. Your browser will download a file named for the report date range. The file is plain C S V, so you can open it directly in Excel, or import it into any reporting tool. The columns are client, first name, last name, account number, notes, date, and rep. One important thing to know: the on-screen view is limited to twenty thousand rows, but the C S V export has no such limit. For large date ranges or full portfolio reports, always use the C S V download to make sure you have the complete data set.
5. [If you see no results] If your report shows no results, or you're not sure about your date range, first check your dates, and clear the debtor filter. If you still see nothing, reach out to your account manager.

### debtor-status: How to look up debtor status (2:30)
1. [Open Debtor Status] The Debtor Status screen lets you look up the current standing of any account in your portfolio. You can search for a single debtor by account number or name, or run a broader report filtered by placement date or payment date range. Results are displayed in an interactive grid, with expandable payment and promise history. Click View Debtor Status in the left sidebar. The search dialog gives you two ways to find accounts: by account or name for a single record, or by date range for multiple records. These two modes cannot be combined.
2. [Search by account or name] To search by account number or name, type at least two characters into the Account or Debtor Name field. The portal will suggest matching records as you type. Selecting a suggestion fills both fields automatically. Leave the Date Filter on All, and click Search.
3. [Search by date range] To search by date range, select Placement Date Range or Payment Date Range from the Date Filter dropdown. The Account and Name fields will clear automatically. Use the quick buttons, or enter custom dates. Date range searches show up to one thousand records. A blank, full portfolio search has the same one thousand record limit.
4. [Read the results grid] Search results display in a grid showing key financial and status information for each debtor. The columns are debtor name, account number, current debt, original debt, opened, paid to date, attempts, status, and actions. A negative current debt, shown in parentheses, means an overpayment or a credit. The report header shows the date range and filter type used, and Back returns you to the portal dashboard. These screens use sample data.
5. [What each status means] Status is color-coded for quick scanning. Green is Paid in Full. The full original balance has been collected. Gold is Settled in Full. The account closed at a negotiated amount less than the original balance. Red is Restricted. The account has been flagged with a restriction, so contact your account manager for details. Blue is Active. The account is in active collection. Gray is Other. Various other statuses may appear, depending on account circumstances.

### debtor-history: Debtor profile, payments and promises (1:23)
1. [Debtor profile] Each row in the results grid can have up to three action icons in the Actions column. Icons only appear when the relevant data exists for that debtor. The person icon opens the Debtor Profile popup, showing full contact details, address, phone, email, assigned amount, and account dates. Click the X, or click outside the popup, to close it.
2. [Payment history] The dollar icon expands Payment History inline, under the debtor row, showing post date, amount, discount, reference, balance, and payment type. No dollar icon means no payments have posted. Click it again to collapse.
3. [Promise history] The P icon expands Promise History inline, under the debtor row, showing promises to pay, including dates, amounts, delivery method, and whether the promise was kept or broken. No P icon means no promise has been recorded. Rows open and close independently, so you can compare accounts side by side.

### upload-files: How to upload files to SWRS (2:16)
1. [Open Upload New Debtors] The Secure File Exchange gives you a safe, encrypted way to send files to Southwest Recovery Services, and receive documents back. No email required. All transfers go through the portal, which is especially important for any files containing debtor records, account numbers, or other sensitive information. To send a file, click the Upload New Debtors button in the action bar at the top of your dashboard. Despite the name, this tool accepts any file type: placement data, invoices, contracts, or supporting documents. In the upload dialog, start by entering a file description, to help the S W R S processing team identify what you've sent. Something like, April twenty twenty-six new placements, or invoice ten forty-two supporting docs, works great.
2. [Choose and send] Next, click Choose Files, and select one or more files from your computer. Hold Control on Windows, or Command on a Mac, to select multiple files at once. When you're ready, click Send File, and wait for the success confirmation before closing the dialog.
3. [Wait for the success message] Once the upload is complete, you'll see a confirmation message showing how many files were sent. The dialog stays open, so you can send additional files without reopening it. The S W R S processing team is notified automatically. You don't need to call or email to confirm receipt.
4. [File rules] A few rules. File names must be unique, and each file must be under twenty megabytes. Avoid special characters in names, and include a date. Accepted formats are Excel, preferred for placements, plus CSV, Word, PDF, and plain text. If a file is over twenty megabytes, contact your account manager. If you uploaded the wrong file, contact us as soon as possible and tell us which one to disregard. Don't upload a corrected version with the same file name.

### document-vault: How to get statements and documents (1:17)
1. [Find the vault button] When Southwest Recovery Services has a report or document ready for your account, a Secure Document Vault button will appear in your action bar. This button is only visible when files are actually available. If you don't see it, there are simply no documents waiting for you at this time.
2. [Download your file] Click Secure Document Vault to open the client library. All documents currently available for your account will be listed here, typically named with a description and timestamp. Click Download next to any file to save it to your computer. Each file has its own download button, so you can grab just what you need.
3. [Links last 30 minutes] One important thing to keep in mind: download links are active for thirty minutes from the time you open the vault. If a link expires before you download, just close the vault and reopen it to generate fresh links. If you're expecting a document that isn't listed, reach out to your account manager. Use the contact information at the end of this video.

### new-placements: How to place new accounts (2:43)
1. [Two ways to send debtor information] The portal gives you two ways to submit debtor information to Southwest Recovery Services. Upload New Debtors is for submitting multiple new accounts at once, using a formatted spreadsheet. It accepts Excel and C S V files, supports multiple files per session, and replaces the need to email placement files to your rep. Update Current Debtors is for sending a correction note or supporting document for an account that's already in the system. This video covers new placements.
2. [Download the right template] Before submitting new placements, you'll need the right template. Click Download File Templates in the left sidebar to open the template library. There are two options. The General New Debtors template is an Excel spreadsheet, where each row represents one debtor. Use this for regular batch placements. The Single Debtor template is a Word document for one account that requires more detail than the spreadsheet allows. Fill in your template completely before uploading.
3. [What to have ready] A few things to have ready for each account: the debtor's full legal name, last known address, original account number and balance, date of last payment or date of service, contact information if available, and any special handling instructions.
4. [Upload the placement file] Once your placement template is filled out, click Upload New Debtors in the action bar at the top of your dashboard. Start with a clear file description, something like, May twenty twenty-six new placements, forty-two accounts. This helps the processing team triage your file quickly. Click Choose Files, and select your completed template. If you have multiple files, hold Control on Windows, or Command on a Mac, to select them all at once. Click Send File, and wait for the success confirmation before closing the dialog. The S W R S team is notified automatically. No need to call or email to confirm receipt.
5. [Bulk placement tips] A few things to keep in mind before you upload. Use the official S W R S template, and don't add, remove, or reorder any columns. Use one row per debtor, with no merged cells or summary rows. And make sure each file has a unique name, as the portal won't accept two files with the same filename. For very large batches, or accounts with special handling requirements, check with your account manager before uploading, to confirm the correct process.

### update-account: How to update a current account (1:43)
1. [Update a current account] If you need to send a correction note or supporting document for an account already in the system, click Update Current Debtors in your action bar. The update form has a few required fields. Enter the account number. The field supports autocomplete, so start typing, and matching accounts from your portfolio will appear as suggestions. You can also search by debtor last name or company name. Selecting a suggestion automatically fills in the account number for you. Enter your name, so the S W R S team knows who submitted the update, and your email address, in case they have follow-up questions. In the additional information field, describe what has changed or what action you need taken. Be as specific as possible. This goes directly to your representative. If you have a supporting document to include, use the optional Attach a File field to add one: an agreement, a corrected invoice, or any other relevant document. Then click Submit Update. The update routes directly to your rep. You don't need to follow up separately.
2. [Common questions] If you don't use the template, any file format will upload, but the template avoids delays. If an account doesn't show in autocomplete, type at least two characters. It may not be in the system yet, so submit it as a new placement. If you submitted the wrong file, contact us right away, before it's processed.

### direct-payment: How to report a direct payment (3:20)
1. [What is a direct payment?] A direct payment occurs when a debtor pays your organization directly, rather than through Southwest Recovery Services. When this happens, it's important to report it through the portal as soon as possible, so S W R S can update the account balance, close the account if it's been paid in full, and keep collections accurately reconciled. Reporting promptly matters. Delays can result in a debtor being contacted for a balance that's already been paid, which reflects poorly on your organization.
2. [When to report, and when not to] So when should you report a direct payment? Anytime a debtor mails a check to your office, pays in person, pays through your own payment portal, or when an insurance provider pays you directly. You should also report partial payments, and any settlements you accept directly. What you don't need to report: any payment that was made through the S W R S portal, collected by S W R S on your behalf, or that already appears in the Recent Payments panel on your dashboard. If you're ever unsure, check with your account manager before submitting.
3. [Fill in the form] Click Report A Direct Payment in the action bar. Type the account number or the debtor's last name or company name, and pick a suggestion. It fills in both fields. Enter the exact payment amount you received. For a partial payment, enter only what you actually received. Then enter the payment date, which is the date you received the payment, not the date you're reporting it.
4. [Write Off Amount: an example] Write Off Amount. If a debtor has settled their account for less than the full balance owed, you'll need to use the Write Off Amount field. This represents the portion of the debt your organization is agreeing to forgive as part of the settlement. For example, if a debtor owes five hundred dollars, negotiates a settlement, and pays three hundred fifty dollars, you would enter three hundred fifty as the Payment Amount, and one hundred fifty as the Write Off Amount. This allows S W R S to close the account correctly, and reconcile the full original balance. If you're not sure whether a write-off applies, leave the field blank, and contact your account manager before submitting.
5. [Attach proof, then submit] Attaching a file is optional, but strongly recommended. It speeds up processing, and reduces the chance of follow-up questions from the S W R S team. Accepted formats include P D F, J P G, P N G, Word documents, and Excel files, up to twenty megabytes each. Good things to attach include a remittance slip, a copy of the check front, a bank deposit confirmation, or a settlement agreement. When in doubt, attach it. Then click Submit Payment.
6. [If something looks wrong] If you reported the wrong amount, contact us as soon as possible with the correct details. Don't submit a second payment report for the same account. If the account doesn't show in autocomplete, type at least two characters. If it still doesn't appear, it may not be in the system yet, so contact your account manager.

## Code

### topics.py
```python
# Per-topic video definitions. Scene types: img, cards. Title and end scenes are added automatically.
TOPICS=[
{"id":"login","title":"How to log in","sub":"Sign in to the Client Portal","scenes":[
 {"t":"img","title":"Sign in","img":"login.png","steps":[("Go to <b>swrsportal.com</b>",""),("Enter your <b>Username</b>",""),("Enter your <b>Password</b>",""),("Click <b>Login</b>","You land on your dashboard.")],
  "say":"To sign in, go to S W R S portal dot com. On the Client Portal Login screen, enter the username assigned to your portal account, then your password. Click Login, and you land on your dashboard. If you've never logged in and need your first credentials, contact your account manager."},
 {"t":"img","title":"Forgot your password?","img":"login.png","steps":[("Click <b>Forgot password?</b>","Under the Login button."),("Follow the reset steps","See the video: How to reset your password.")],
  "say":"If you can't remember your password, click Forgot password, just under the Login button. We have a separate short video that walks you through the reset. If your account is locked after several failed attempts, contact us and we'll unlock it."},
 {"t":"cards","title":"Two portal roles","cols":2,"items":[("Standard user","View activity reports. Look up debtor status. Upload files. Report direct payments. Use the Secure Document Vault."),("Manager","Everything a standard user can do. Plus switch between client accounts and run consolidated manager reports.")],
  "say":"Your access depends on your role. Standard users can view activity reports, look up debtor status, upload files, report direct payments, and use the Secure Document Vault. Managers can do all of that, plus switch between client accounts and run consolidated manager reports. To add a user or change a role, email info at S W recovery dot com with the person's name, email address, and the role you need."},
]},
{"id":"reset-password","title":"How to reset your password","sub":"Takes about two minutes","scenes":[
 {"t":"img","title":"Start the reset","img":"login.png","steps":[("Open <b>swrsportal.com</b>",""),("Click <b>Forgot password?</b>","Under the Login button.")],
  "say":"Forgot your password? Go to the login page and click Forgot password. The reset has two confirmation steps, and the whole thing takes about two minutes."},
 {"t":"img","title":"Request the reset","img":"forgot.png","steps":[("Enter your email","The email registered to your portal account."),("Click <b>Send Confirmation Email</b>","")],
  "say":"Enter the email address registered to your portal account, and click Send Confirmation Email."},
 {"t":"img","title":"Confirm the request","img":"confirmemail.png","steps":[("Open the email from <b>PortalS@swrecovery.com</b>","Subject: Confirm your password reset request"),("Click <b>Confirm password reset</b>","Didn't ask for a reset? Ignore the email.")],
  "say":"Check your inbox for an email from Portal S at S W recovery dot com. The subject is Confirm your password reset request. Click Confirm password reset. If you didn't request a reset, just ignore the email and your password won't change."},
 {"t":"img","title":"Confirm on the portal","img":"confirmpage.png","steps":[("Click <b>Confirm Password Reset</b>","The portal then sends a second email with your reset link.")],
  "say":"A confirmation page opens in your browser. Click Confirm Password Reset. The portal now sends a second email, with your actual reset link."},
 {"t":"img","title":"Open the reset link","img":"resetemail.png","steps":[("Open the second email","From PortalS@swrecovery.com. Subject: Reset your password."),("Click <b>Reset password</b>","")],
  "say":"Open the second email, from the same sender, with the subject Reset your password. Click Reset password."},
 {"t":"img","title":"Set your new password","img":"newpw.png","steps":[("Enter a <b>New password</b>","At least 8 characters."),("<b>Confirm</b> the new password",""),("Click <b>Set New Password</b>","Do this promptly. The link expires soon after it is sent.")],
  "say":"Enter your new password, then enter it again to confirm. It must be at least eight characters. Click Set New Password. Do this promptly, because the reset link expires soon after it's sent. Then log in at S W R S portal dot com with your new password."},
 {"t":"cards","title":"If something goes wrong","cols":3,"items":[("No email?","Check spam or junk. Add PortalS@swrecovery.com to your safe senders list."),("Still nothing after 5 minutes?","Start the reset again, or contact support."),("Link expired?","Start over from the login page. The whole sequence only takes a couple of minutes.")],
  "say":"If an email doesn't arrive, check your spam or junk folder, and add Portal S at S W recovery dot com to your safe senders list. If nothing arrives after five minutes, start the reset again, or contact support. If a link says it has expired, start over from the login page."},
]},
{"id":"profile-mfa","title":"My Profile and MFA","sub":"Turn on a one-time email code, and change your password","scenes":[
 {"t":"img","title":"Open My Profile","img":"profile.png","steps":[("Click <b>My Profile</b>","Left sidebar of your dashboard."),("Two things to manage","Multi-factor authentication (MFA), and your password.")],
  "say":"Click My Profile in the left sidebar of your dashboard. Your username and email address show at the top. If either needs to change, reach out to your account manager. Below that are two sections: multi-factor authentication, called MFA, and Change Password."},
 {"t":"img","title":"Turn on MFA","img":"mfapanel.png","steps":[("Check <b>Enable MFA (email one-time code)</b>","A panel opens with your registered email."),("Click <b>Send Code</b>","")],
  "say":"We strongly recommend MFA. It adds a second layer of security to your login. To turn it on, check the box that says Enable MFA, email one-time code. A panel opens showing the email address where your codes will be sent. That's the email registered to your account. Click Send Code."},
 {"t":"cards","title":"Check your email","cols":2,"items":[("6-digit code","Sent from PortalS@swrecovery.com. Don't share it with anyone."),("Expires in 10 minutes","Enter it promptly. Each new code replaces the previous one.")],
  "say":"A six-digit code arrives from Portal S at S W recovery dot com. Don't share it with anyone. The code expires in ten minutes."},
 {"t":"img","title":"Verify your login","img":"verify.png","steps":[("Type the 6-digit code",""),("Click <b>Verify</b>",""),("Code expired or missing? Click <b>Resend code</b>","Check spam first.")],
  "say":"Type the six-digit code on the Verify your login page, and click Verify. If the code expired or never arrived, click Resend code. Check your spam folder first, and remember that each new code replaces the one before it."},
 {"t":"img","title":"MFA is active","img":"mfagreen.png","steps":[("Look for the green <b>MFA is active</b> panel",""),("From now on","After your username and password, you enter a code from your email."),("To turn it off","Uncheck the box. It turns off immediately.")],
  "say":"When it works, you return to My Profile and see a green panel saying MFA is active. From then on, you'll get a six-digit code by email each time you sign in, after your username and password. To turn MFA off, uncheck the box. It turns off immediately, but it does lower the security of your account."},
 {"t":"img","title":"Change your password","img":"profile.png","steps":[("Find <b>Change Password</b>","Bottom of My Profile."),("Enter your <b>current</b> password",""),("Enter and confirm a <b>new</b> password","At least 8 characters."),("Click <b>Change Password</b>","It takes effect immediately.")],
  "say":"To change your password, scroll to the Change Password section. Enter your current password, then your new password twice. It must be at least eight characters. Click Change Password, and it takes effect immediately. If you've forgotten your current password, use Forgot password on the login page instead."},
]},
{"id":"reports","title":"How to run an activity report","sub":"Date range, filters and CSV export","scenes":[
 {"t":"img","title":"Open the report","img":"report.png","steps":[("Click <b>View Activity Report</b>","Left sidebar."),("Choose a date range","This Week, This Month, This Year, or custom From and To dates.")],
  "say":"The Debtor Activity Report shows the notes and actions recorded on your accounts for a date range. Click View Activity Report in the left sidebar. Choose This Week, This Month, or This Year, and the dates fill in for you. Or enter your own From and To dates. The report supports up to three hundred sixty-six days, and asks you to confirm anything longer than a year."},
 {"t":"img","title":"Filter by debtor (optional)","img":"report.png","steps":[("Set <b>Search By</b>","Last Name, First Name, or Account #."),("Type a value in <b>Contains</b>",""),("Leave both blank","To run the report for every debtor."),("Click <b>View Report</b>","")],
  "say":"To narrow the report to one debtor, set Search By to last name, first name, or account number, and type a value in Contains. Leave both blank to run the report for your whole portfolio. Then click View Report."},
 {"t":"img","title":"Read the results","img":"reportgrid_20.png","steps":[("Sorted by debtor last name",""),("Each row","Debtor name, account number, date and time, and a note."),("Debtors appear more than once","One note for the email sent, one for the workflow that triggered it. That's normal.")],
  "say":"The results are sorted by debtor last name. Each row shows the debtor name, account number, the date and time, and a note about what happened. You'll see each debtor more than once. One note is for the email sent, and one is for the automated workflow that triggered it. Both are captured for audit purposes, so that's completely normal."},
 {"t":"img","title":"Export to CSV","img":"reportgrid_20.png","steps":[("Click <b>Download CSV</b>","Top right of the report."),("Open it in Excel","Columns: Client, First Name, Last Name, Account #, Notes, Date, Rep."),("Need every record?","The screen stops at 20,000 rows. The CSV is not capped.")],
  "say":"To export, click Download CSV at the top right. Your browser downloads a plain CSV file, named for the report date range. You can open it in Excel, with the client, first and last name, account number, notes, date, and the assigned rep. The on-screen view stops at twenty thousand rows, but the CSV includes every matching record."},
 {"t":"cards","title":"If you see no results","cols":2,"items":[("Check your dates","Make sure the date range is the one you meant."),("Clear the debtor filter","Run the report for all debtors to confirm there is activity. Still nothing? Contact your account manager.")],
  "say":"If the report shows no results, first check your date range. Then clear the debtor filter and run it for all debtors. If you still see nothing, or you're not sure about your date range, contact your account manager."},
]},
{"id":"debtor-status","title":"How to look up debtor status","sub":"Search, status meanings and history","scenes":[
 {"t":"img","title":"Open Debtor Status","img":"status.png","steps":[("Click <b>View Debtor Status</b>","Left sidebar."),("One record","Search by Account or Debtor Name."),("Many records","Search by Date Range.")],
  "say":"Click View Debtor Status in the left sidebar. You can search two ways. For a single record, search by account number or debtor name. For many records, search by date range. The two can't be combined."},
 {"t":"img","title":"Search by account or name","img":"status.png","steps":[("Type 2 or more characters","In Account or Debtor Name."),("Pick a suggestion","It fills both fields."),("Click <b>Search</b>","Leave Date Filter on All.")],
  "say":"Type at least two characters into the Account or Debtor Name field. Suggestions appear as you type. Pick one, and it fills in both fields. Leave the Date Filter on All, and click Search."},
 {"t":"img","title":"Search by date range","img":"status.png","steps":[("Choose a <b>Date Filter</b>","Placement Date Range, or Payment Date Range."),("Pick the dates","This Week, This Month, This Year, or custom."),("Up to 1,000 records","Leaving everything blank runs your full portfolio, with the same cap.")],
  "say":"For a date range, choose Placement Date Range, which is when the account was placed, or Payment Date Range, which is when payments posted. Use the quick buttons or enter custom dates. Date range searches show up to one thousand records. Leaving everything blank with the filter on All runs your full portfolio, with the same one thousand limit."},
 {"t":"img","title":"Read the results grid","img":"statusgrid.png","steps":[("Columns","Debtor Name, Account #, Current Debt, Original Debt, Opened, Paid to Date, Attempts, Status, Actions."),("Negative current debt","Shown in parentheses. It means an overpayment or credit.")],
  "say":"The results grid shows debtor name, account number, current debt, original debt, the date opened, paid to date, attempts, status, and actions. A negative current debt, shown in parentheses, means an overpayment or a credit. These screens use sample data."},
 {"t":"cards","title":"What each status means","cols":3,"items":[("Paid in Full (green)","The full original balance has been collected."),("Settled in Full (gold)","Closed at a negotiated amount below the original balance."),("Restricted (red)","The account has a restriction applied. Contact your account manager for details."),("Active (blue)","The account is in active collection."),("Other (gray)","Various other statuses may appear depending on account circumstances.")],
  "say":"Status is color-coded for quick scanning. Paid in Full, shown in green, means the full original balance has been collected. Settled in Full, shown in gold, means the account closed at a negotiated amount below the original balance. Restricted, shown in red, means the account has a restriction applied, so contact your account manager for details. Active, shown in blue, means the account is in active collection. Gray means other, and various other statuses may appear depending on the account."},
 {"t":"img","title":"Debtor profile","img":"statuspopup.png","steps":[("Click the <b>person</b> icon","Opens the Debtor Profile popup."),("See","Contact details, account details, and a financial summary."),("Close with <b>×</b>","Or click outside the popup.")],
  "say":"Each row can have up to three action icons, and they only appear when there's data. The person icon opens the Debtor Profile, with contact details, account dates, and a financial summary. Click the X, or click outside the popup, to close it."},
 {"t":"img","title":"Payment history","img":"statuspay.png","steps":[("Click the <b>$</b> icon","Payment History opens under the row."),("See","Post date, amount, discount, reference, balance, settled flag, type."),("Click <b>$</b> again","To collapse it.")],
  "say":"The dollar icon expands Payment History right under the row. You'll see the post date, amount, discount, reference, balance, whether it settled, and the payment type. No dollar icon means no payments have posted. Click it again to collapse."},
 {"t":"img","title":"Promise history","img":"statuspromise.png","steps":[("Click the <b>P</b> icon","Promise History opens under the row."),("See","Dates, type, delivery method, amount promised and paid, broken, active."),("Rows open independently","Compare several accounts at once.")],
  "say":"The P icon expands Promise History. It shows when each promise was made and due, the type, how it was delivered, the amount promised and paid, and whether it was broken or is still active. No P icon means no promise to pay has been recorded. Payment and promise rows open and close independently, so you can compare accounts side by side."},
]},
{"id":"upload-files","title":"How to upload files to SWRS","sub":"Secure file upload, limits and formats","scenes":[
 {"t":"img","title":"Open Upload New Debtors","img":"fileupload.png","steps":[("Use the portal, not email","Especially for files with debtor information."),("Click <b>Upload New Debtors</b>","It accepts any file type, not only placements."),("Enter a <b>File Description</b>","Example: April 2026 new placements.")],
  "say":"The portal gives you a safe, encrypted way to send files to us. No email required. That matters most for files with debtor information. Click Upload New Debtors in the action bar. Despite the name, it accepts any file type: placement data, invoices, contracts, or supporting documents. Enter a short file description, like April 2026 new placements."},
 {"t":"img","title":"Choose and send","img":"fileupload.png","steps":[("Click <b>Choose Files</b>","Hold Ctrl or Cmd to select several."),("Click <b>Send File</b>","The dialog stays open for more uploads.")],
  "say":"Click Choose Files and select your file. Hold Control on Windows, or Command on a Mac, to pick more than one. Then click Send File."},
 {"t":"img","title":"Wait for the success message","img":"uploadok.png","steps":[("Look for <b>Success! Uploaded N file(s)</b>","The count is cumulative for the session."),("SWRS is notified automatically","No need to call or email to confirm receipt.")],
  "say":"Wait for the success message before you close the window. It says how many files were uploaded, and that count adds up across the session. Our team is notified automatically, so there's no need to call or email to confirm."},
 {"t":"cards","title":"File rules","cols":2,"items":[("Name and size","Unique file names. Under 20 MB per file. Avoid special characters, and include a date in the name."),("Accepted formats","xls and xlsx (preferred for placements), csv, doc and docx, pdf, txt."),("Over 20 MB?","Contact your account manager to arrange another way to send it."),("Wrong file?","Contact SWRS as soon as possible and say which file to disregard. Don't re-upload with the same name.")],
  "say":"A few rules. File names must be unique, and each file must be under twenty megabytes. Avoid special characters in names, and include a date. Accepted formats are Excel, preferred for placements, plus CSV, Word, PDF, and plain text. If a file is over twenty megabytes, contact your account manager. If you uploaded the wrong file, contact us as soon as possible and tell us which one to disregard. Don't upload a corrected version with the same file name."},
]},
{"id":"document-vault","title":"How to get statements and documents","sub":"The Secure Document Vault","scenes":[
 {"t":"img","title":"Find the vault button","img":"vaulthome.png","steps":[("Look for <b>Secure Document Vault</b>","In the action bar at the top of your dashboard."),("No button?","Then no files are waiting for your account right now.")],
  "say":"When we've prepared a statement, report, or document for your account, a Secure Document Vault button appears in the action bar at the top of your dashboard. The button only appears when files are ready. If you don't see it, nothing is waiting for you right now."},
 {"t":"img","title":"Download your file","img":"vaultlib.png","steps":[("Click <b>Secure Document Vault</b>","The Client Library opens."),("Find your file","Named with a description and a timestamp."),("Click <b>Download</b>","Each file has its own button.")],
  "say":"Click the button to open your Client Library. Your documents are listed with a description and a timestamp. Click Download next to the file you need. It saves to your default downloads folder."},
 {"t":"img","title":"Links last 30 minutes","img":"vaultlib.png","steps":[("Download links stay active for <b>30 minutes</b>","From the time you open the vault."),("Link expired?","Close the Client Library, then click Secure Document Vault again for fresh links."),("Document not listed?","Contact your account manager.")],
  "say":"Download links are active for thirty minutes from the time you open the vault. If a link expires, close the Client Library and click Secure Document Vault again to get fresh links. If you're expecting a document that isn't listed, contact your account manager."},
]},
{"id":"new-placements","title":"How to place new accounts and send updates","sub":"Templates, bulk upload, and Update Current Debtors","scenes":[
 {"t":"cards","title":"Two ways to send debtor information","cols":2,"items":[("Upload New Debtors","Best for several new accounts at once. Use the SWRS placement template. Excel or CSV. Up to 20 MB per file."),("Update Current Debtors","Best for a correction, update, or note on an account already in the system. Routes directly to your rep.")],
  "say":"There are two ways to send debtor information through the portal. Upload New Debtors is for submitting new accounts, several at a time, using the SWRS placement template. Update Current Debtors is for sending a correction, an update, or a note about an account that's already in the system. Both replace email."},
 {"t":"img","title":"Download the right template","img":"templates.png","steps":[("Click <b>Download File Templates</b>","Left sidebar."),("<b>General New Debtors Template</b>","Excel. One row per debtor."),("<b>Single Debtor Template</b>","Word. One account that needs more detail.")],
  "say":"Before you submit new placements, click Download File Templates in the left sidebar. The General New Debtors Template is an Excel spreadsheet, with one row per debtor, for regular batch placements. The Single Debtor Template is a Word document for one account that needs more detail than the spreadsheet allows. Fill it in, then upload it through the portal. Don't email the completed template."},
 {"t":"cards","title":"What to have ready","cols":2,"items":[("Debtor","Full legal name. Last known address."),("Account","Original account number and balance. Date of last payment or date of service."),("Contact","Phone and email, if available."),("Special handling","Any special handling instructions.")],
  "say":"Have this ready: the debtor's full legal name and last known address, the original account number and balance, the date of last payment or date of service, phone and email if you have them, and any special handling instructions."},
 {"t":"img","title":"Upload the placement file","img":"fileupload.png","steps":[("Click <b>Upload New Debtors</b>",""),("Describe the file","Example: May 2026 new placements, 42 accounts."),("<b>Choose Files</b>, then <b>Send File</b>","Wait for the success message.")],
  "say":"Click Upload New Debtors. Enter a descriptive file description, like May 2026 new placements, forty-two accounts. Choose your completed template, click Send File, and wait for the success message. Our team is notified automatically."},
 {"t":"cards","title":"Bulk placement tips","cols":2,"items":[("Keep the template as is","Don't add, remove, or reorder columns."),("One row per debtor","No merged cells and no summary rows."),("Unique file names","You can't upload two files with the same name."),("Very large batches","Contact your account manager before you upload.")],
  "say":"A few tips for bulk placements. Use the General New Debtors Template, and don't add, remove, or reorder columns. Use one row per debtor, with no merged cells or summary rows. Give every file a unique name, and confirm the success message before you close the window. For very large batches or special handling, contact your account manager first."},
 {"t":"img","title":"Update a current account","img":"update.png","steps":[("Click <b>Update Current Debtors</b>",""),("Account Number, Debtor Last Name or Company Name","Type to search. Suggestions fill in both."),("Your name and email","So we can follow up."),("Describe the change. Attach a file if helpful.","Then click <b>Submit Update</b>.")],
  "say":"To send a correction or note about an existing account, click Update Current Debtors. Enter the account number, or the debtor's last name or company name. Suggestions fill in both fields. Enter your name and email so we can follow up, describe what changed or what you need, and attach one supporting document if it helps. Then click Submit Update. The update goes directly to your rep, so you don't need to follow up separately."},
 {"t":"cards","title":"Common questions","cols":3,"items":[("No template?","Any file format uploads, but the template avoids delays. Other files may need manual reformatting."),("Account not in autocomplete?","Type at least 2 characters. It may not be in the system yet. Submit it as a new placement."),("Submitted the wrong file?","Contact SWRS right away, before the file is processed.")],
  "say":"If you don't use the template, any file format will upload, but the template avoids delays. If an account doesn't show in autocomplete, type at least two characters. It may not be in the system yet, so submit it as a new placement. If you submitted the wrong file, contact us right away, before it's processed."},
]},
{"id":"direct-payment","title":"How to report a direct payment","sub":"When a debtor pays you directly","scenes":[
 {"t":"cards","title":"What is a direct payment?","cols":1,"items":[("A debtor pays your organization instead of SWRS","Report it as soon as possible. We update the balance, close the account if it's paid in full, and reconcile collections. A delay can lead to a debtor being contacted for a balance that's already been paid.")],
  "say":"A direct payment is when a debtor pays your organization directly, instead of going through us. When that happens, report it in the portal as soon as possible, so we can update the balance, close the account if it's paid in full, and reconcile your collections. A delay can lead to a debtor being contacted for a balance that's already been paid."},
 {"t":"cards","title":"When to report, and when not to","cols":2,"items":[("Report when","A debtor mails a check to your office. Pays in person. Pays through your own payment portal. Their insurance pays you directly. You get a partial payment. You accept a settlement directly."),("Do not report when","The payment was made through the SWRS portal. SWRS collected it for you. It already appears in your Recent Payments. You're unsure: check with your account manager first.")],
  "say":"Report a direct payment when a debtor mails a check to your office, pays in person, pays through your own payment portal, or when their insurance pays you directly. Also report partial payments, and settlements you accept directly. Don't report a payment made through the SWRS portal, a payment we collected for you, or one that already appears in your Recent Payments. If you're unsure, check with your account manager first."},
 {"t":"img","title":"Fill in the form","img":"directpay.png","steps":[("Click <b>Report A Direct Payment</b>","Action bar at the top of your dashboard."),("<b>Account Number</b> and <b>Debtor Name</b>","Required. Pick a suggestion and it fills in both."),("<b>Payment Amount</b>","Required. The exact amount you received."),("<b>Payment Date</b>","Required. The date you received it, not today's date.")],
  "say":"Click Report A Direct Payment in the action bar. Type the account number or the debtor's last name or company name, and pick a suggestion. It fills in both fields. Enter the exact payment amount you received. For a partial payment, enter only what you actually received. Then enter the payment date, which is the date you received the payment, not the date you're reporting it."},
 {"t":"cards","title":"Write Off Amount: an example","cols":1,"items":[("A debtor owes $500.00 and settles for $350.00","Payment Amount: $350.00. Write Off Amount: $150.00. Leave Write Off blank for a standard full or partial payment. Not sure it applies? Leave it blank and ask your account manager before you submit.")],
  "say":"Write Off Amount is optional. Use it when a debtor settles for less than the full balance, and you're forgiving the difference. For example, a debtor owes five hundred dollars and settles for three hundred fifty. Enter three hundred fifty as the Payment Amount, and one hundred fifty as the Write Off Amount. For a standard full or partial payment, leave it blank. If you're not sure a write-off applies, leave it blank and ask your account manager before you submit."},
 {"t":"img","title":"Attach proof, then submit","img":"directpay.png","steps":[("Attach a file","Optional but recommended: remittance slip, check copy (front only), deposit confirmation, settlement agreement, or insurance EOB."),("Formats","PDF, JPG, PNG, DOCX, XLSX. Up to 20 MB per file."),("Click <b>Submit Payment</b>","")],
  "say":"Attaching a file is optional, but strongly recommended. It speeds up processing. Good choices are a remittance slip, a copy of the check, front only, a bank deposit confirmation, a settlement agreement, or an insurance explanation of benefits. Accepted formats are PDF, JPG, PNG, Word, and Excel, up to twenty megabytes per file. When you're done, click Submit Payment."},
 {"t":"cards","title":"If something looks wrong","cols":2,"items":[("Wrong amount?","Contact SWRS as soon as possible with the correct details. Don't submit a second payment report for the same account."),("Account not in autocomplete?","Type at least 2 characters. If it still doesn't appear, it may not be in the system yet. Contact your account manager.")],
  "say":"If you reported the wrong amount, contact us as soon as possible with the correct details. Don't submit a second payment report for the same account. If the account doesn't show in autocomplete, type at least two characters. If it still doesn't appear, it may not be in the system yet, so contact your account manager."},
]},
]
END_SAY="Still need help? Call eight, six, six. Eight, three, seven. Three, zero, six, five. Or email info at S W recovery dot com. We're here Monday through Friday, eight A M to five P M Central."

# --- split long topics so each video covers one short process ---
def _split():
    out=[]
    for t in TOPICS:
        if t['id']=='debtor-status':
            a=dict(t,sub="Search, then read the results grid",scenes=t['scenes'][:5])
            b={"id":"debtor-history","title":"Debtor profile, payments and promises","sub":"Use the action icons in Debtor Status","scenes":t['scenes'][5:]}
            out+= [a,b]
        elif t['id']=='new-placements':
            a=dict(t,title="How to place new accounts",sub="Templates and bulk upload",scenes=t['scenes'][:5])
            b={"id":"update-account","title":"How to update a current account","sub":"Send a correction or note through the portal","scenes":t['scenes'][5:]}
            out+= [a,b]
        else: out.append(t)
    return out
TOPICS=_split()

# --- v3: narration rewritten from the Vimeo training-video transcripts (stt/*.txt). Corrections: no case-sensitivity claim; support contact = 866-837-3065 / info@swrecovery.com ---
_SAY={
('login',0):"To access the Southwest Recovery Services client portal, open your browser and go to S W R S portal dot com. On the login screen, enter the username assigned to your portal account, then enter your password. When you're ready, click Login. You'll be taken directly to your dashboard.",
('login',1):"If this is your first time logging in and you haven't received your initial credentials, reach out to your account manager, and they'll get you set up. If you've forgotten your password, click Forgot password. We have a separate short video for that. If your account becomes locked after multiple failed login attempts, contact the S W R S support team to have it unlocked. Use the phone number or email at the end of this video.",
('reset-password',0):"If you've forgotten your password, click the Forgot Password link on the login page. This opens the reset request form. The reset has two confirmation steps, and takes about two minutes.",
('reset-password',1):"Enter the email address registered to your portal account, and click Send Confirmation Email. If an account exists for that address, you'll receive the first email in the reset sequence within a few minutes.",
('reset-password',2):"Check your inbox for a message from Portal S at S W recovery dot com, with the subject line, Confirm Your Password Reset Request. Open that email, and click the Confirm Password Reset link. This verifies that you made the request, and opens a confirmation page in your browser. If you didn't request a reset, simply ignore the email. Your password won't be changed.",
('reset-password',3):"On that confirmation page, click the Confirm Password Reset button to complete the verification step. The portal will then send you a second email with your actual reset link.",
('reset-password',4):"After you confirm on the portal page, a second email will arrive with the subject line, Reset your password. Open that email, and click the Reset Password link. This takes you to the New Password form. Complete this step promptly. The link expires shortly after it's sent.",
('reset-password',5):"On the form, enter your new password. It must be at least eight characters. Re-enter it in the confirm field, then click Set New Password. That's it. You can now log in at S W R S portal dot com with your new password.",
('reset-password',6):"One helpful tip. If either email doesn't show up within a few minutes, check your spam or junk folder. Both emails come from Portal S at S W recovery dot com, so adding that address to your safe senders list will prevent future filtering. If nothing arrives after five minutes, start the reset again, or contact support. If a link has expired, start over from the login page.",
('profile-mfa',0):"The My Profile page is where you manage your personal portal settings. To access it, click My Profile in the left sidebar of your dashboard. At the top, you'll see your username and email address. These are the credentials registered to your portal account. If either needs to be updated, reach out to your account manager. Below that are two sections: Multi-Factor Authentication, which lets you enable or disable email verification for your logins, and Change Password, which lets you update your portal password at any time. The Back to Home link returns you to your dashboard without making any changes.",
('profile-mfa',1):"Multi-Factor Authentication, or M F A, adds a second layer of security to your login. When enabled, you'll receive a six-digit verification code by email each time you sign in. We strongly recommend enabling it on all portal accounts. To get started, check the Enable M F A checkbox on the My Profile page. The setup panel will expand, showing the email address where your codes will be sent. Click Send Code.",
('profile-mfa',2):"You'll be taken to the verification page, and a six-digit code will arrive in your inbox from Portal S at S W recovery dot com. Don't share the code with anyone. The code expires in ten minutes, so enter it promptly.",
('profile-mfa',3):"Enter that code, and click Verify. If it expires before you get to it, just click Resend Code to get a fresh one. Each new code replaces the one before it.",
('profile-mfa',4):"Once verified, you'll be returned to My Profile, and a green confirmation panel will show that M F A is now active on your account. To turn M F A off, uncheck the box. It turns off immediately.",
('reports',0):"The Debtor Activity Report lets you view all notes and actions recorded against your accounts for any date range you choose. To get started, click View Activity Report in the left sidebar of your portal dashboard. This opens the filter dialog. You have two ways to set your date range. The quick select buttons, This Week, This Month, and This Year, automatically fill in the From and To fields for you. Or if you need a specific window, enter your own custom From and To dates. The report supports ranges up to three hundred sixty-six days, and will prompt you to confirm anything longer than a year.",
('reports',1):"You can also narrow your results to a specific debtor. Set the Search By field to Last Name, First Name, or Account Number. Then type a value in the Contains field. If you want to see your full portfolio, leave both fields blank. When you're ready, click View Report. Your results will load in the same window.",
('reports',2):"Once your report loads, you'll see every recorded note and action for your accounts within the selected date range, sorted alphabetically by debtor last name. The report header shows the date range the report was run for, along with a back link, so you can return to the filter dialog. Each row is a single activity record. It shows the debtor name, account number, the date and time of the activity, and a note describing what happened, such as an email sent, a workflow triggered, or a payment posted. Some debtors appear more than once, and that's completely normal. One row is the direct email sent to the debtor, and another is the automated workflow it triggered. Both are captured for audit purposes.",
('reports',3):"To export your report, click the Download C S V button in the top right corner of the results page. Your browser will download a file named for the report date range. The file is plain C S V, so you can open it directly in Excel, or import it into any reporting tool. The columns are client, first name, last name, account number, notes, date, and rep. One important thing to know: the on-screen view is limited to twenty thousand rows, but the C S V export has no such limit. For large date ranges or full portfolio reports, always use the C S V download to make sure you have the complete data set.",
('reports',4):"If your report shows no results, or you're not sure about your date range, first check your dates, and clear the debtor filter. If you still see nothing, reach out to your account manager.",
('debtor-status',0):"The Debtor Status screen lets you look up the current standing of any account in your portfolio. You can search for a single debtor by account number or name, or run a broader report filtered by placement date or payment date range. Results are displayed in an interactive grid, with expandable payment and promise history. Click View Debtor Status in the left sidebar. The search dialog gives you two ways to find accounts: by account or name for a single record, or by date range for multiple records. These two modes cannot be combined.",
('debtor-status',1):"To search by account number or name, type at least two characters into the Account or Debtor Name field. The portal will suggest matching records as you type. Selecting a suggestion fills both fields automatically. Leave the Date Filter on All, and click Search.",
('debtor-status',2):"To search by date range, select Placement Date Range or Payment Date Range from the Date Filter dropdown. The Account and Name fields will clear automatically. Use the quick buttons, or enter custom dates. Date range searches show up to one thousand records. A blank, full portfolio search has the same one thousand record limit.",
('debtor-status',3):"Search results display in a grid showing key financial and status information for each debtor. The columns are debtor name, account number, current debt, original debt, opened, paid to date, attempts, status, and actions. A negative current debt, shown in parentheses, means an overpayment or a credit. The report header shows the date range and filter type used, and Back returns you to the portal dashboard. These screens use sample data.",
('debtor-status',4):"Status is color-coded for quick scanning. Green is Paid in Full. The full original balance has been collected. Gold is Settled in Full. The account closed at a negotiated amount less than the original balance. Red is Restricted. The account has been flagged with a restriction, so contact your account manager for details. Blue is Active. The account is in active collection. Gray is Other. Various other statuses may appear, depending on account circumstances.",
('debtor-history',0):"Each row in the results grid can have up to three action icons in the Actions column. Icons only appear when the relevant data exists for that debtor. The person icon opens the Debtor Profile popup, showing full contact details, address, phone, email, assigned amount, and account dates. Click the X, or click outside the popup, to close it.",
('debtor-history',1):"The dollar icon expands Payment History inline, under the debtor row, showing post date, amount, discount, reference, balance, and payment type. No dollar icon means no payments have posted. Click it again to collapse.",
('debtor-history',2):"The P icon expands Promise History inline, under the debtor row, showing promises to pay, including dates, amounts, delivery method, and whether the promise was kept or broken. No P icon means no promise has been recorded. Rows open and close independently, so you can compare accounts side by side.",
('upload-files',0):"The Secure File Exchange gives you a safe, encrypted way to send files to Southwest Recovery Services, and receive documents back. No email required. All transfers go through the portal, which is especially important for any files containing debtor records, account numbers, or other sensitive information. To send a file, click the Upload New Debtors button in the action bar at the top of your dashboard. Despite the name, this tool accepts any file type: placement data, invoices, contracts, or supporting documents. In the upload dialog, start by entering a file description, to help the S W R S processing team identify what you've sent. Something like, April twenty twenty-six new placements, or invoice ten forty-two supporting docs, works great.",
('upload-files',1):"Next, click Choose Files, and select one or more files from your computer. Hold Control on Windows, or Command on a Mac, to select multiple files at once. When you're ready, click Send File, and wait for the success confirmation before closing the dialog.",
('upload-files',2):"Once the upload is complete, you'll see a confirmation message showing how many files were sent. The dialog stays open, so you can send additional files without reopening it. The S W R S processing team is notified automatically. You don't need to call or email to confirm receipt.",
('new-placements',0):"The portal gives you two ways to submit debtor information to Southwest Recovery Services. Upload New Debtors is for submitting multiple new accounts at once, using a formatted spreadsheet. It accepts Excel and C S V files, supports multiple files per session, and replaces the need to email placement files to your rep. Update Current Debtors is for sending a correction note or supporting document for an account that's already in the system. This video covers new placements.",
('new-placements',1):"Before submitting new placements, you'll need the right template. Click Download File Templates in the left sidebar to open the template library. There are two options. The General New Debtors template is an Excel spreadsheet, where each row represents one debtor. Use this for regular batch placements. The Single Debtor template is a Word document for one account that requires more detail than the spreadsheet allows. Fill in your template completely before uploading.",
('new-placements',2):"A few things to have ready for each account: the debtor's full legal name, last known address, original account number and balance, date of last payment or date of service, contact information if available, and any special handling instructions.",
('new-placements',3):"Once your placement template is filled out, click Upload New Debtors in the action bar at the top of your dashboard. Start with a clear file description, something like, May twenty twenty-six new placements, forty-two accounts. This helps the processing team triage your file quickly. Click Choose Files, and select your completed template. If you have multiple files, hold Control on Windows, or Command on a Mac, to select them all at once. Click Send File, and wait for the success confirmation before closing the dialog. The S W R S team is notified automatically. No need to call or email to confirm receipt.",
('new-placements',4):"A few things to keep in mind before you upload. Use the official S W R S template, and don't add, remove, or reorder any columns. Use one row per debtor, with no merged cells or summary rows. And make sure each file has a unique name, as the portal won't accept two files with the same filename. For very large batches, or accounts with special handling requirements, check with your account manager before uploading, to confirm the correct process.",
('update-account',0):"If you need to send a correction note or supporting document for an account already in the system, click Update Current Debtors in your action bar. The update form has a few required fields. Enter the account number. The field supports autocomplete, so start typing, and matching accounts from your portfolio will appear as suggestions. You can also search by debtor last name or company name. Selecting a suggestion automatically fills in the account number for you. Enter your name, so the S W R S team knows who submitted the update, and your email address, in case they have follow-up questions. In the additional information field, describe what has changed or what action you need taken. Be as specific as possible. This goes directly to your representative. If you have a supporting document to include, use the optional Attach a File field to add one: an agreement, a corrected invoice, or any other relevant document. Then click Submit Update. The update routes directly to your rep. You don't need to follow up separately.",
('document-vault',0):"When Southwest Recovery Services has a report or document ready for your account, a Secure Document Vault button will appear in your action bar. This button is only visible when files are actually available. If you don't see it, there are simply no documents waiting for you at this time.",
('document-vault',1):"Click Secure Document Vault to open the client library. All documents currently available for your account will be listed here, typically named with a description and timestamp. Click Download next to any file to save it to your computer. Each file has its own download button, so you can grab just what you need.",
('document-vault',2):"One important thing to keep in mind: download links are active for thirty minutes from the time you open the vault. If a link expires before you download, just close the vault and reopen it to generate fresh links. If you're expecting a document that isn't listed, reach out to your account manager. Use the contact information at the end of this video.",
('direct-payment',0):"A direct payment occurs when a debtor pays your organization directly, rather than through Southwest Recovery Services. When this happens, it's important to report it through the portal as soon as possible, so S W R S can update the account balance, close the account if it's been paid in full, and keep collections accurately reconciled. Reporting promptly matters. Delays can result in a debtor being contacted for a balance that's already been paid, which reflects poorly on your organization.",
('direct-payment',1):"So when should you report a direct payment? Anytime a debtor mails a check to your office, pays in person, pays through your own payment portal, or when an insurance provider pays you directly. You should also report partial payments, and any settlements you accept directly. What you don't need to report: any payment that was made through the S W R S portal, collected by S W R S on your behalf, or that already appears in the Recent Payments panel on your dashboard. If you're ever unsure, check with your account manager before submitting.",
('direct-payment',3):"Write Off Amount. If a debtor has settled their account for less than the full balance owed, you'll need to use the Write Off Amount field. This represents the portion of the debt your organization is agreeing to forgive as part of the settlement. For example, if a debtor owes five hundred dollars, negotiates a settlement, and pays three hundred fifty dollars, you would enter three hundred fifty as the Payment Amount, and one hundred fifty as the Write Off Amount. This allows S W R S to close the account correctly, and reconcile the full original balance. If you're not sure whether a write-off applies, leave the field blank, and contact your account manager before submitting.",
('direct-payment',4):"Attaching a file is optional, but strongly recommended. It speeds up processing, and reduces the chance of follow-up questions from the S W R S team. Accepted formats include P D F, J P G, P N G, Word documents, and Excel files, up to twenty megabytes each. Good things to attach include a remittance slip, a copy of the check front, a bank deposit confirmation, or a settlement agreement. When in doubt, attach it. Then click Submit Payment.",
}
_ST={t['id']:t for t in TOPICS}
for (tid,i),txt in _SAY.items(): _ST[tid]['scenes'][i]['say']=txt
# slide text aligned to the new narration
_ST['login']['scenes'][1].update(title="First time, forgot it, or locked out?",steps=[("Never logged in?","Contact your account manager for your initial credentials."),("Forgot your password?","Click <b>Forgot password?</b> under the Login button. See the reset video."),("Account locked?","Happens after several failed attempts. Contact SWRS support to unlock it.")])
_ST['profile-mfa']['scenes'][0].update(steps=[("Click <b>My Profile</b>","Left sidebar of your dashboard."),("Username and email at the top","These are registered to your account. To change either, contact your account manager."),("Two sections below","Multi-Factor Authentication and Change Password. <b>Back to Home</b> returns you to the dashboard.")])
_ST['profile-mfa']['scenes'][1].update(steps=[("MFA adds a second layer of security","A six-digit code is emailed each time you sign in. Strongly recommended."),("Check <b>Enable MFA (email one-time code)</b>","A panel opens with the email where codes are sent."),("Click <b>Send Code</b>","")])
_ST['debtor-status']['scenes'][4]['items']=[("Paid in Full (green)","The full original balance has been collected."),("Settled in Full (gold)","Closed at a negotiated amount below the original balance."),("Restricted (red)","The account has been flagged with a restriction. Contact your account manager for details."),("Active (blue)","The account is in active collection."),("Other (gray)","Various other statuses may appear depending on account circumstances.")]

```

### tts.py
```python
import importlib.util, hashlib, json, pathlib, time, urllib.request, concurrent.futures as cf
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
VOICE='hpp4J3VqNfWAUOO0d1Us'
(B/'audio3').mkdir(exist_ok=True)
def tts(text):
    h=hashlib.md5(text.encode()).hexdigest()[:12]; out=B/'audio3'/f'{h}.mp3'
    if out.exists() and out.stat().st_size>2000: return str(out)
    body=json.dumps({"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.7,"similarity_boost":0.75,"style":0.0,"use_speaker_boost":True,"speed":0.96}}).encode()
    for a in range(4):
        try:
            r=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128',data=body,headers={'xi-api-key':KEY,'Content-Type':'application/json','Accept':'audio/mpeg'})
            d=urllib.request.urlopen(r,timeout=120).read(); out.write_bytes(d); return str(out)
        except Exception as e:
            err=str(e).replace(KEY,'***'); time.sleep(3*(a+1))
    raise RuntimeError('tts failed: '+err)
texts=[]
for t in m.TOPICS:
    t['intro']=f"{t['title']}. {t['sub']}."
    texts.append(t['intro'])
    for sc in t['scenes']: texts.append(sc['say'])
texts.append(m.END_SAY)
texts=list(dict.fromkeys(texts))
with cf.ThreadPoolExecutor(6) as ex: res=dict(zip(texts,ex.map(tts,texts)))
json.dump(res,open(B/'audio_map3.json','w'))
print(len(res),'clips')

```

### slides2.py
```python
import asyncio, pathlib, importlib.util, json, re
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
ms=importlib.util.spec_from_file_location('ms',B/'make_slides_lib.py');
from playwright.async_api import async_playwright
CSS="""
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;font-family:'Fira Sans','Helvetica Neue',Arial,sans-serif;background:linear-gradient(135deg,#0D2B4E 0%,#143a66 100%);color:#fff;overflow:hidden;position:relative}
.brand{position:absolute;left:96px;top:56px;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#cfe0f5;font-weight:500}
.brand b{color:#E8740C}
.left{position:absolute;left:96px;top:140px;width:720px;height:800px}
h1{font-size:68px;line-height:1.06;font-weight:700;margin-bottom:36px}
.step{display:flex;gap:22px;align-items:flex-start;margin-bottom:24px}
.num{flex:0 0 52px;height:52px;border-radius:50%;background:#E8740C;color:#fff;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;margin-top:2px}
.step p{font-size:34px;line-height:1.25;color:#f2f7fd}
.step p small{display:block;font-size:26px;line-height:1.3;color:#aac4e4;margin-top:4px}
.card{position:absolute;right:80px;top:110px;width:1000px;height:820px;border-radius:24px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;overflow:hidden;padding:20px}
.card img{max-width:100%;max-height:100%;border-radius:12px}
.foot{position:absolute;left:96px;bottom:44px;font-size:24px;color:#9fb9da}
.foot b{color:#fff}
.bar{position:absolute;left:0;bottom:0;height:10px;width:100%;background:#E8740C}
.center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 120px}
.big{font-size:128px;font-weight:700;color:#E8740C;margin:26px 0 10px}
.mid{font-size:48px;color:#fff}
.ctitle{position:absolute;left:96px;top:130px;right:96px;font-size:68px;font-weight:700;line-height:1.05}
.grid{position:absolute;left:96px;right:96px;top:260px;height:670px;display:grid;gap:28px;align-content:center}
.c{background:rgba(255,255,255,.09);border:2px solid rgba(255,255,255,.16);border-left:10px solid #E8740C;border-radius:18px;padding:30px 34px;min-width:0}
.c h3{font-size:46px;color:#fff;margin-bottom:12px;line-height:1.15}
.c p{font-size:36px;line-height:1.35;color:#d7e5f6}
.kick{font-size:30px;color:#E8740C;letter-spacing:.12em;text-transform:uppercase;font-weight:700;margin-bottom:26px}
"""
FOOT='<div class="foot">Still need help? Call <b>866-837-3065</b> or email <b>info@swrecovery.com</b> (Mon-Fri, 8 AM-5 PM CT)</div><div class="bar"></div>'
BR='<div class="brand">Southwest Recovery Services <b>&middot;</b> Client Portal</div>'
def steps(items):
    return ''.join(f'<div class="step"><div class="num">{i}</div><p>{t}'+(f'<small>{sm}</small>' if sm else '')+'</p></div>' for i,(t,sm) in enumerate(items,1))
def imgslide(sc): return f'{BR}<div class="left"><h1>{sc["title"]}</h1>{steps(sc["steps"])}</div><div class="card"><img src="file://{B}/img/{sc["img"]}"></div>{FOOT}'
def cardslide(sc):
    cols=sc.get('cols',2); n=len(sc['items'])
    cs=''.join(f'<div class="c"><h3>{a}</h3><p>{b}</p></div>' for a,b in sc['items'])
    return f'{BR}<div class="ctitle">{sc["title"]}</div><div class="grid" style="grid-template-columns:repeat({cols},1fr);{"font-size:1.15em" if cols==1 else ""}">{cs}</div>{FOOT}'
def title(t): return f'{BR}<div class="center"><div class="kick">How-to video</div><h1 style="font-size:104px;margin-bottom:34px">{t["title"]}</h1><div class="mid" style="color:#cfe0f5">{t["sub"]}</div></div><div class="bar"></div>'
END=f'{BR}<div class="center"><div class="mid">Still need help?</div><div class="big">866-837-3065</div><div class="mid">info@swrecovery.com</div><div class="mid" style="color:#aac4e4;margin-top:22px;font-size:38px">Mon-Fri, 8 AM-5 PM CT</div></div><div class="bar"></div>'
FIT="""()=>{const out=[];
 for(const sel of ['.left','.grid']){const el=document.querySelector(sel);if(!el)continue;
  let k=0;const lim=el.getBoundingClientRect().top+(sel==='.left'?800:670);
  const kids=[...el.querySelectorAll('h1,h3,p,small')];
  const base=new Map(kids.map(x=>[x,parseFloat(getComputedStyle(x).fontSize)]));
  let f=1;
  while(f>0.55){const last=el.lastElementChild.getBoundingClientRect().bottom;const sh=el.scrollHeight>el.clientHeight+2;
    if(last<=lim&&!sh)break; f-=0.04; kids.forEach(x=>x.style.fontSize=(base.get(x)*f)+'px');}
  out.push([sel,f]);}
 return out}"""
async def main():
    (B/'slides2').mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1920,'height':1080})
        async def shot(name,html):
            f=B/'slides2'/f'{name}.html'; f.write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{html}')
            await pg.goto(f'file://{f}'); await pg.wait_for_timeout(200)
            r=await pg.evaluate(FIT)
            await pg.screenshot(path=str(B/'slides2'/f'{name}.png')); return r
        for t in m.TOPICS:
            await shot(f'{t["id"]}_title',title(t))
            for i,sc in enumerate(t['scenes']):
                r=await shot(f'{t["id"]}_{i}',imgslide(sc) if sc['t']=='img' else cardslide(sc))
                if r and r[0][1]<0.85: print('shrunk',t['id'],i,r)
        await shot('end',END)
        await b.close()
asyncio.run(main())

```

### assemble.py
```python
import importlib.util, json, pathlib, subprocess, concurrent.futures as cf
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
A=json.load(open(B/'audio_map3.json'))
(B/'seg3').mkdir(exist_ok=True); (B/'out3').mkdir(exist_ok=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
def clip(png,aud,out):
    d=dur(aud)+0.6
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','25','-i',png,'-i',aud,'-t',f'{d:.2f}','-af','loudnorm=I=-16:TP=-1.5:LRA=9,apad','-vf',f'fade=t=in:st=0:d=0.25,fade=t=out:st={d-0.25:.2f}:d=0.25,format=yuv420p','-c:v','libx264','-crf','20','-preset','veryfast','-r','25','-c:a','aac','-b:a','160k','-ar','44100','-ac','2',out],check=True)
    return d
jobs=[];plans={}
for t in m.TOPICS:
    items=[(f'slides2/{t["id"]}_title.png',A[f"{t['title']}. {t['sub']}."],f'seg3/{t["id"]}_title.mp4')]
    for i,sc in enumerate(t['scenes']): items.append((f'slides2/{t["id"]}_{i}.png',A[sc['say']],f'seg3/{t["id"]}_{i}.mp4'))
    items.append(('slides2/end.png',A[m.END_SAY],f'seg3/{t["id"]}_end.mp4'))
    plans[t['id']]=items; jobs+=items
with cf.ThreadPoolExecutor(4) as ex: res=list(ex.map(lambda j: clip(str(B/j[0]),j[1],str(B/j[2])),jobs))
dmap={j[2]:r for j,r in zip(jobs,res)}
meta={}
for t in m.TOPICS:
    lst=B/f'seg3/{t["id"]}.txt'; lst.write_text(''.join(f"file '{B/i[2]}'\n" for i in plans[t['id']]))
    out=B/'out3'/f'SWRS_Portal_{t["id"]}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(lst),'-c','copy','-movflags','+faststart',str(out)],check=True)
    ch=[];c=0
    for i in plans[t['id']]: ch.append(c); c+=dmap[i[2]]
    meta[t['id']]={'file':out.name,'dur':round(dur(str(out)),1),'size_mb':round(out.stat().st_size/1e6,1),'chapters':[round(x,1) for x in ch]}
    print(t['id'],meta[t['id']]['dur'],meta[t['id']]['size_mb'])
json.dump(meta,open(B/'out/meta.json','w'),indent=1)

```

### stt.py
```python
import glob, json, os, subprocess, uuid, urllib.request, concurrent.futures as cf, pathlib
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
def run(f):
    n=pathlib.Path(f).stem.rsplit('_',1)[0]
    mp3=f'stt/{n}.mp3'; subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vn','-ac','1','-ar','16000','-b:a','48k',mp3],check=True)
    b=uuid.uuid4().hex; data=open(mp3,'rb').read()
    parts=[('model_id','scribe_v1'),('timestamps_granularity','word'),('tag_audio_events','false')]
    body=b''
    for k,v in parts: body+=f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    body+=f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode()+data+f'\r\n--{b}--\r\n'.encode()
    r=urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text',data=body,headers={'xi-api-key':KEY,'Content-Type':f'multipart/form-data; boundary={b}'})
    try: j=json.load(urllib.request.urlopen(r,timeout=300))
    except Exception as e: return n,'ERR '+str(e).replace(KEY,'***')
    open(f'stt/{n}.json','w').write(json.dumps(j)); open(f'stt/{n}.txt','w').write(j.get('text',''))
    return n,j.get('text','')
with cf.ThreadPoolExecutor(4) as ex:
    for n,t in ex.map(run,sorted(glob.glob('vid/*.mp4'))): print('==',n,'\n',t,'\n')

```

### rt.py
```python
import json,subprocess,uuid,urllib.request,re,difflib,importlib.util,pathlib,concurrent.futures as cf
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
B=pathlib.Path('build')
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def stt(f):
    mp3=f'stt/rt_{pathlib.Path(f).stem}.mp3'; subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vn','-ac','1','-ar','16000','-b:a','48k',mp3],check=True)
    b=uuid.uuid4().hex; d=open(mp3,'rb').read(); body=b''
    for k,v in [('model_id','scribe_v1'),('tag_audio_events','false')]: body+=f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    body+=f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode()+d+f'\r\n--{b}--\r\n'.encode()
    r=urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text',data=body,headers={'xi-api-key':KEY,'Content-Type':f'multipart/form-data; boundary={b}'})
    return json.load(urllib.request.urlopen(r,timeout=300))['text']
def norm(t): return re.findall(r"[a-z0-9']+",t.lower())
def one(t):
    got=stt(f'build/out3/SWRS_Portal_{t["id"]}.mp4')
    exp=f"{t['title']}. {t['sub']}. "+' '.join(x['say'] for x in t['scenes'])+' '+m.END_SAY
    a,b=norm(exp),norm(got); r=difflib.SequenceMatcher(None,a,b).ratio()
    miss=[(x[0],' '.join(a[x[1]:x[2]]),' '.join(b[x[3]:x[4]])) for x in difflib.SequenceMatcher(None,a,b).get_opcodes() if x[0]!='equal']
    return t['id'],round(r,3),[x for x in miss if not re.search(r"swrecovery|s w|a m|p m|portal|\b(and|it|2026|six|three)\b|multi|sw",str(x))]
with cf.ThreadPoolExecutor(4) as ex:
    for i,r,mi in ex.map(one,m.TOPICS): print(i,r,mi)

```
