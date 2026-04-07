from models import Email

POLICY_SNIPPETS = """
ENTERPRISE INBOX POLICY
1. Spam & Phishing: Archive all emails asking for passwords, gift cards, or sending suspicious links (unless it looks like a targeted internal phishing attack spoofing executives, in which case forward to security@company.com).
2. Invoices & Billing: Forward all vendor invoices and billing questions to billing@company.com.
3. Job Applications: Forward any resumes or job inquiries to hr@company.com.
4. Vendor Inquiries: If a vendor asks about partnership or onboarding, reply back stating exactly: "Please fill out our Vendor Partnership Form at company.com/vendor-form".
"""

TASKS = {
    "easy": [
        {
            "email": Email(id="e_e1", sender="suspicious_prince@scam.com", subject="URGENT: Inherit $10M", body="Please send your bank details to claim your fortune."),
            "truth": {"action_type": "archive"}
        },
        {
            "email": Email(id="e_e2", sender="candidate@gmail.com", subject="Application for Software Engineer", body="Attached is my resume for the open SWE role."),
            "truth": {"action_type": "forward", "target_email": "hr@company.com"}
        },
        {
            "email": Email(id="e_e3", sender="vendor_invoice@acme.com", subject="Invoice #4922", body="Hello, attached is the invoice for last month's supplies."),
            "truth": {"action_type": "forward", "target_email": "billing@company.com"}
        }
    ],
    "medium": [
        {
            "email": Email(id="e_m1", sender="sales@newvendor.com", subject="Partnership Opportunity", body="We would like to become a vendor for your company. What is the process?"),
            "truth": {"action_type": "reply", "keyword": "company.com/vendor-form"}
        },
        {
            "email": Email(id="e_m2", sender="ceo_spoof@gmail.com", subject="Urgent: Apple Gift Cards", body="I am in a meeting, I need you to buy 5 $100 apple gift cards and send the codes."),
            "truth": {"action_type": "forward", "target_email": "security@company.com"}
        },
        {
            "email": Email(id="e_m3", sender="intern@university.edu", subject="Summer Internship", body="I am looking for a summer internship in the design team."),
            "truth": {"action_type": "forward", "target_email": "hr@company.com"}
        },
        {
            "email": Email(id="e_m4", sender="accounting@aws.amazon.com", subject="AWS Overdue Invoice", body="Please pay your overdue invoice of $4,500 immediately to avoid suspension."),
            "truth": {"action_type": "forward", "target_email": "billing@company.com"}
        },
        {
            "email": Email(id="e_m5", sender="services@crm.com", subject="How to become a partner?", body="We offer new CRM tools, how do we partner with you?"),
            "truth": {"action_type": "reply", "keyword": "company.com/vendor-form"}
        }
    ],
    "hard": [
        # 10 mixed emails replicating medium + more complex variations
        {
            "email": Email(id="e_h1", sender="ceo_spoof@gmail.com", subject="Urgent: Apple Gift Cards", body="I am in a meeting, I need you to buy 5 $100 apple gift cards and send the codes."),
            "truth": {"action_type": "forward", "target_email": "security@company.com"}
        },
        {
            "email": Email(id="e_h2", sender="sales@newvendor.com", subject="Partnership Opportunity", body="We would like to become a vendor for your company. What is the process?"),
            "truth": {"action_type": "reply", "keyword": "company.com/vendor-form"}
        },
        {
            "email": Email(id="e_h3", sender="candidate2@gmail.com", subject="Resume - Data Scientist", body="My resume is attached."),
            "truth": {"action_type": "forward", "target_email": "hr@company.com"}
        },
        {
            "email": Email(id="e_h4", sender="newsletter@marketing.com", subject="Top 10 Tech Trends", body="Read our latest blog post on tech trends!"),
            "truth": {"action_type": "archive"}
        },
        {
            "email": Email(id="e_h5", sender="billing@stripe.com", subject="Receipt for Transaction", body="Here is the receipt for your recent Stripe transaction."),
            "truth": {"action_type": "forward", "target_email": "billing@company.com"}
        },
        {
            "email": Email(id="e_h6", sender="admin@it-support-portal.scam.company.com", subject="Reset your password", body="Your password has expired. Click here to reset: http://bit.ly/123"),
            "truth": {"action_type": "forward", "target_email": "security@company.com"}
        },
        {
            "email": Email(id="e_h7", sender="random@spam.com", subject="Buy cheap pills", body="Cheapest pills on the internet!"),
            "truth": {"action_type": "archive"}
        },
        {
            "email": Email(id="e_h8", sender="vendor@supplier.com", subject="Onboarding form", body="Hi, we are interested in onboarding as a new supplier."),
            "truth": {"action_type": "reply", "keyword": "company.com/vendor-form"}
        },
        {
            "email": Email(id="e_h9", sender="invoices@docusign.net", subject="Signature Requested", body="Please sign the attached invoice from ACME corp."),
            "truth": {"action_type": "forward", "target_email": "billing@company.com"}
        },
        {
            "email": Email(id="e_h10", sender="recruiter@agency.com", subject="Great candidate for your team", body="I have a senior engineer looking for a role, can we chat?"),
            "truth": {"action_type": "forward", "target_email": "hr@company.com"}
        }
    ]
}
