#Python Automation Deck

---

#Python strengths

-Fixed/well defined scenarios

-Low development time

-Rich library helps with flexibility

Following slides will discuss broad types of automations, with a spotlight on the exciting ones

---

#Web automations

There are various sites that may need multiple clicks to get all relevant data. Checking data for bids posted on sites, creating tickets, web scraping and form fills can all be done via python scripts.

---

#Web automation spotlight: HP link generation



Created for BOS team

We have carepacks in bulk. We want to send them to customers. Issue is that the link that is generated for us contains the bulk amount, which we don't want to forward. HP gives a way to delegate links to smaller chunks, which is a lengthy form filling phase.

There are cases where we have 1000 packs, while what is needed is 500 alloted in 100 links(5 per link). So instead of filling the form 100 times, the script logs in, cycles through the form data and captures the created links. These links then can be shared via the excel output that contains all 100 links. This process is fairly autonomous.

---

Human form filling will take around 150 seconds per link generation. Script takes roughly 11 seconds. This time reduces further the more bulk cases we receive(best test cases went to roughly 9 seconds).

Since HP does not have any way to allow for this link splitting natively, this is a novel service offered by RPtech, allowing for more bulk orders and speeding up the process further.

---

#Excel automations

Python is great at number crunching at scale, working on whole columns at a time. Excel is also a convenient output format for various bulk tasks, making a majority of python tasks starting/ending up with Excel files.

---

#Excel automation spotlight-(Excel not exciting) Ageing Report

Created for SAP team? Finance team? Sujata ma'am

Part of Accounts master report, this is the first step. The report sorts materials based on when they were purchased. Input consists of all materials we currently have, script then keeps on going to SAP to figure out under which of the following buckets the materials fall under: Purchased within a year, material-to-material transfer, production, returned from customer and finally Ageing(not purchased within a year).

---

This script does not save time, in fact we could argue it takes more time than a person would to generate this report. We are looking at opportunity cost with this script.

The process is lengthy, requiring a lot of data(querying all materials and when they were purchased asks a lot from SAP). Any human mistakes is costly as it derails the process. Which might not seem that bad, without taking into account when it's run: Quarter end.

The time when the team has multiple other tasks. Asking a person to not make mistakes while multitasking and then ask another to confirm if the data is correct during that critical time...

This script keeps the team a little sane. Fully automated. Something went wrong? Start it up and see the results next morning.

---

#PDF extraction

A lot of the documents we deal with (invoices, bills, notices) are in PDF format. As a growing company the number of these keep on increasing, promting a better way to "read" these files.

Python does the reading, crunches up calculations, creates columns and presents in as an Excel file(our preferred way to deal with bulk).

---

#PDF extraction spotlight: Claim team automation

Yet...to...be...delivered to Claims team

Takes in current data we have on claims, then matches it with the PDFs sent to us. Checks whether the details of the claim(product details, quantities, prices) match what we have and concocts them to flag any errors. Name didn't match? This PDF that should have come didn't? We got 2 PDFs for the same claim? Flagged

---

Will add more details once I actually deliver :)
