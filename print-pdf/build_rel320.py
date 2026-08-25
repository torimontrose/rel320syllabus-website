# -*- coding: utf-8 -*-
# Exact verbatim text from the live REL 320 site. Same compact system as
# FYW 1323, restyled in REL 320's own plum/copper palette and display serif.
import sys
sys.path.insert(0, "/private/tmp/claude-504/-Users-vmontrose-Desktop-FYW-1323-What-is-a-cult-syllabus-website/b73c8ee0-12b2-4b38-8bba-44ab21e5fc8f/scratchpad/syllabus-pdfs")
from gen_schedule import sched_table
from rel320_data import rows as sched_rows

OUT = "/private/tmp/claude-504/-Users-vmontrose-Desktop-FYW-1323-What-is-a-cult-syllabus-website/b73c8ee0-12b2-4b38-8bba-44ab21e5fc8f/scratchpad/syllabus-pdfs/rel320-syllabus.html"

TOKENS = """
:root {
  --paper: #ffffff;
  --ink: #1c1522;
  --ink-soft: #6b5d70;
  --dark: #1c1522;
  --on-dark: #f5ece2;
  --on-dark-soft: #cbbfce;
  --accent-a: #9c5e28;
  --accent-strong: #8a4a1f;
  --accent-b: #6b3f5e;
  --line: #e2d9de;
  --callout-bg: #f6f1f4;
  --photo-bg: #f8f4f6;
  --accent-mark: #e0a35f;
  --font-display: "Cormorant Garamond", serif;
  --font-body: "Work Sans", sans-serif;
}
body { background: #ffffff; }
mark { color: #1c1522 !important; }
a { color: var(--accent-a); }
"""

HEAD = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>REL 320 Syllabus</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="print-system.css">
<style>{TOKENS}</style>
</head><body>
"""

RUNHEAD = '<div class="runhead">Fall 2026 &middot; Furman University &middot; REL 320</div>'

def item(heading, body_html):
    return f'<div class="item"><h4>{heading}</h4><div class="prose">{body_html}</div></div>'

pages = []

# ---------------- PAGE 1: COVER ----------------
pages.append(f"""
<div class="page">
  <div class="cover-hero">
    <div class="cover-eyebrow">Fall 2026 &middot; Furman University</div>
    <h1 class="cover-title" style="font-size:46px;">SEXUALITY &amp;<br>GENDER IN BUDDHISM</h1>
    <p class="cover-subtitle">Reading against the grain to recover gender, sexuality, and marginalized voices across two millennia of Buddhist traditions &mdash; REL 320</p>
  </div>
  <div class="pad" style="margin-top:0.32in;">
    <div style="display:flex; justify-content:center;">
      <div style="width:3.6in;">
        <div style="border:2px solid var(--accent-a); padding:5px;">
          <img src="rel320-cover.jpeg" style="width:100%; display:block;">
        </div>
        <p class="photo-credit" style="text-align:center; margin-top:6px;">The N&#257;ga King&rsquo;s Daughter, from the Lotus Sutra &mdash; read in Week 6</p>
      </div>
    </div>
    <div class="cols2" style="margin-top:0.3in;">
      <div class="side-head" style="grid-template-columns:1.1in 3px 1fr;">
        <div class="label" style="font-size:16px;">Course<br>Info</div>
        <div class="rule"></div>
        <div class="body prose">
          <p><strong>Meets:</strong> Tue / Thu, 11:30 AM&ndash;12:45 PM &middot; Furman Hall 201</p>
          <p><strong>Instructor:</strong> Dr. Tori Montrose<br>victoria.montrose@furman.edu</p>
          <p><strong>Office:</strong> Furman Hall 206J &middot; Office hours by appointment</p>
        </div>
      </div>
      <div class="prose">
        <p style="font-style:italic; color:var(--ink-soft);">&ldquo;How does Buddhism reinforce, affirm, challenge, or complicate gender roles and understandings of sexuality in the broader cultural context?&rdquo;</p>
      </div>
    </div>
  </div>
</div>
""")

# ---------------- PAGE 2: DESCRIPTION, TEXTS, OUTCOMES ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.3in;">
    <div class="sec-title">Course Description &amp; Learning Outcomes</div>
    <div class="prose">
      <p>This course explores cultural, social, philosophical, and historical dimensions of sexuality and gender within Buddhist traditions across the globe. We examine sutras, novels, poetry, biographies, memoirs, art, and film that span over two millennia to investigate Buddhist approaches to gender and gender roles, understandings of femininity and masculinity, views on the body, ideas about family structures, desire, and sexuality. This course will also look at how contemporary Buddhists of color and LGBTQI+ Buddhists have grappled with issues of intersectionality and no-self in terms of their own identities. Examining these topics will often require us to read &ldquo;against the grain&rdquo; in order to mine for marginalized voices. Some guiding questions include: how does Buddhism reinforce, affirm, challenge, or complicate gender roles and understandings of sexuality in the broader cultural context? How are the Buddhist struggle for liberation and women&rsquo;s struggle for liberation from inequality and patriarchal oppression interconnected?</p>
      <p><em>Note: Prior coursework in Buddhism is not required to be successful in this course. We will be reviewing Buddhism&rsquo;s basic ideas and timeline of its development in the first few weeks of the course.</em></p>
    </div>

    <h4 class="block-title" style="margin-top:0.18in;">Course Texts</h4>
    <ul class="prose" style="font-size:11.5px; line-height:1.5;">
      <li><strong>Required:</strong> Alice Collett. <em>I Hear Her Words: An Introduction to Women in Buddhism</em>.</li>
      <li><strong>Recommended:</strong> C. Pierce Salguero. <a href="https://www.penguinrandomhouse.com/books/691081/buddhish-by-c-pierce-salguero/"><em>Buddhish: A Guide to the 20 Most Important Buddhist Ideas for the Curious and Skeptical</em></a>.</li>
    </ul>

    <h4 class="block-title" style="margin-top:0.18in;">Learning Outcomes</h4>
    <div class="cols2">
      <div class="prose">
        <p>We will be able to explain foundational aspects of Buddhism&rsquo;s central ideas &mdash; including ethics, liberatory frameworks, and practices &mdash; with an appreciation for the internal diversity of Buddhism in its various historical and global expressions.</p>
        <p>Using tools from a variety of disciplines used by Buddhist Studies scholars, we will be able to analyze, summarize, and compare Buddhist &ldquo;texts&rdquo; (a &ldquo;text&rdquo; includes practices, sites, and material objects), with a particular focus on the way in which gender and sexuality are represented, constructed, and reinforced within these texts.</p>
      </div>
      <div class="prose">
        <p>We will be able to articulate ways in which Buddhism reinforces, affirms, challenges, or complicates gender roles and understandings of sexuality in the broader cultural context Buddhism finds itself in.</p>
        <p>We will engage in critical self-reflection on our understanding and perception of Buddhism, gender, and sexuality as concepts and identify changes to that understanding over time, ultimately enhancing our ability to dialogue with members of different cultural and religious traditions.</p>
      </div>
    </div>
  </div>
</div>
""")

# ---------------- PAGE 3: GRADING + ASSIGNMENTS ----------------
attendance = item("Attendance and Engagement &mdash; 20%",
  '<p>Every semester of this course is unique to the combination of students that comprise it. For this reason, your presence is an essential part of the learning experience for yourself and all of us in the room with you. This course requires you to come prepared to share your questions, struggles, and ideas surrounding the readings and content we cover. Each student is expected to actively participate in all activities and discussions. There are several ways to demonstrate engagement including small group discussions, taking notes, large group discussions, polls. See the <a href="#policies">Policies tab</a> and the <a href="#rubrics">Engagement Rubric</a>.</p>')

perusall = item("Engagement with Readings on Perusall &mdash; 15%",
  '<p>In addition to the course textbook, weekly readings will be posted to Perusall, which can be accessed through the course Moodle page. Prior to class, you will annotate the day&rsquo;s assigned reading with your comments, questions, observations, and reflections. Perusall comments are time stamped and must be made <strong>by 9am the morning of class</strong> to receive credit. I value the quality of the annotation more than the quantity of annotations you make. Thoughtful responses to classmates&rsquo; comments or questions are also welcomed.</p>')

quizzes = item("Quizzes &mdash; 30% (3 &times; 10%)",
  '<p>Quizzes are given in class (SOAR students should coordinate accommodated testing arrangements in advance). The quizzes change shape over the course of the term. The first quiz will be more multiple choice and term IDs; the second quiz and beyond will include those earlier elements but will also include text/image analysis and short answer/essay. A week before each quiz, you will be given a sheet with guidelines for how best to prepare for the upcoming quiz. Quiz 3 is the final quiz of the term; there is no separate quiz during the scheduled final exam period.</p>')

rrj = item("Reading and Reflection Journal (RRJ) &mdash; 15%",
  '<p>A mix of in-class and at-home short written responses to a prompt about the readings. They will frame your thinking about the readings and help prepare you for in-class discussion or reflect on your learning. Bring your journal to class every day we meet. Unless you have an accommodation, these journals will be handwritten. Journals will be collected every few weeks to check for completion and graded for quality twice this semester. <strong>To be considered complete, each entry must be a minimum of 8 sentences long and must address the prompt.</strong> RRJs missed due to absence can be made up upon return to class. See the <a href="#rubrics">RRJ Rubric</a> for more about expectations.</p>')

bhikkuni = item("Bhikkuni Ordination Game &mdash; Roles and Reflection Paper &mdash; 20%",
  '<p style="font-style:italic; color:var(--ink-soft);">Details will be added later.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.3in;">
    <div class="sec-title" id="graded">Graded Elements</div>
    <div class="sec-kicker">How your final grade is calculated, and what each element involves.</div>
    <table class="weights">
      <thead><tr><th>Component</th><th class="num">Weight</th></tr></thead>
      <tbody>
        <tr><td>Attendance and Engagement</td><td class="num">20%</td></tr>
        <tr><td>Engagement with Readings on Perusall</td><td class="num">15%</td></tr>
        <tr><td>Quizzes (3 &times; 10%)</td><td class="num">30%</td></tr>
        <tr><td>Reading and Reflection Journal (RRJ)</td><td class="num">15%</td></tr>
        <tr><td>Bhikkuni Ordination Game &mdash; Roles and Reflection Paper</td><td class="num">20%</td></tr>
      </tbody>
    </table>
    <h4 class="block-title" style="margin-top:0.15in;">Element Descriptions</h4>
    {attendance}
    {perusall}
    {quizzes}
    {rrj}
    {bhikkuni}
  </div>
</div>
""")

# ---------------- SCHEDULE PAGES ----------------
headers = ["#", "Date", "Reading", "Due/Notes"]
widths = ["0.28in", "0.72in", None, "1.3in"]

def sched_page(title, rows_slice, first=False):
    tb = sched_table(headers, rows_slice, ["reading", "notes"], widths)
    tbar = f'<div class="title-bar" id="schedule">{title}</div>' if first else RUNHEAD
    return f"""
<div class="page">
  {tbar}
  <div class="pad" style="margin-top:0.18in;">{tb}</div>
</div>
"""

chunk1 = sched_rows[0:20]
chunk2 = sched_rows[20:]

pages.append(sched_page("CLASS SCHEDULE", chunk1, first=True))
pages.append(sched_page("", chunk2))

# ---------------- POLICIES ----------------
accessibility = item("Commitment to an Inclusive and Accessible Learning Environment",
  '<p>In the spirit of Universal Design for Learning, I will strive to provide an environment that is equitable and conducive to achievement and learning for all students. I ask that we all be respectful of diverse opinions and of all class members, regardless of personal attribute, and that we all use inclusive language in written and oral work. I encourage persons with Student Office for Accessibility Resources (SOAR) accommodations or other needs that may impact your performance to meet with me promptly to make a plan for the semester.</p>')

absences = item("Policies on Absences and Late Submissions",
  '<p>Students are allowed <strong>3 free absences</strong> (roughly 10% of the total number of classes) regardless of the reason. I do not need you to email me or provide an explanation for these absences. These include absences due to illnesses, personal loss, athletics, religious observances, or any other reason. After 3 absences, your attendance and participation grade will be negatively impacted.</p>'
  '<p><strong>Late submissions</strong> following absences must be submitted on the day of return to class. Otherwise, late submissions of assignments or quizzes may be accepted for partial credit depending on the circumstances.</p>')

integrity = item("Statement on Academic Integrity",
  '<p>Per <a href="https://policies.furman.edu//view.php?policy=584">Section 121.5 of Furman&rsquo;s University Policy</a>, &ldquo;All forms of academic misconduct including cheating, plagiarism, misrepresentation, and unacceptable collaboration are violations of Furman&rsquo;s academic integrity standard. Examples and explanations may be found elsewhere in official university documents (e.g., The Student Handbook and the academic integrity portion of the Furman University website).&rdquo;</p>'
  '<p><strong>Please note:</strong> Students who are suspected of submitting writing produced in any part by an AI system will be subjected to review by the Academic Discipline Committee. For more information on Generative Artificial Intelligence use in this class, see the Use of Generative Artificial Intelligence (AI) policy below.</p>'
  '<p><strong>Note:</strong> Typed assignments must be drafted in a word processor such as Microsoft Word (using the Auto Save to OneDrive feature) or Google Docs that records the document&rsquo;s time-stamped edit history. This edit history, along with TurnItIn&rsquo;s AI detection software, are some of the tools used in assessing cases of AI-related academic integrity concerns. Accordingly, the use of Grammarly and other word processors that rely heavily on AI-based writing suggestions is strongly discouraged.</p>'
  '<p>It is always better to get a zero on an assignment rather than submitting something that violates the university&rsquo;s academic integrity policy, which usually results in far worse consequences.</p>')

recordings = item("Course Activity Recordings",
  '<p>Furman University prohibits the recording of classes by students without obtaining prior, written permission of the instructor, except in cases where Furman permits a qualified student with a documented disability to record classes as a reasonable accommodation. Students are advised of this policy in the Student Handbook. Under no circumstances should recorded classes be used in any way that denigrates and/or decontextualizes the instructor or any student whose class remarks are recorded. Unauthorized dissemination of any recorded classroom proceedings, including distribution for compensation, is strictly prohibited. The improper sharing of recorded material by students or others may constitute a violation of U.S. copyright law and is a violation of campus policy.</p>')

nondiscrim = item("Nondiscrimination Policy and Sexual Misconduct",
  '<p>Furman University and its faculty are committed to supporting our students and seeking an environment that is free of bias, discrimination, and harassment. Furman does not unlawfully discriminate on the basis of race, color, national origin, sex, sexual orientation, gender identity, pregnancy, disability, age, religion, veteran status, or any other characteristic or status protected by applicable local, state, or federal law in admission, treatment, or access to, or employment in, its programs and activities.</p>'
  '<p>If you have encountered any form of discrimination or harassment, including sexual misconduct (e.g. sexual assault, sexual harassment or gender-based harassment, sexual exploitation or intimidation, stalking, intimate partner violence), we encourage you to report this to the institution. If you wish to report such an incident of misconduct, you may contact Furman&rsquo;s Title IX Coordinator, Melissa Nichols (Trone Center, Suite 215; Melissa.nichols@furman.edu; 864.294.2221).</p>'
  '<p>If you would like to speak with someone who can advise you but maintain complete confidentiality, you can talk with a counselor, a professional in the Student Health Center, or someone in the Office of Spiritual Life. If you speak with a faculty member, understand that as a mandated reporter of the University, the faculty member MUST report to the University&rsquo;s Title IX Coordinator what you share to help ensure that your safety and welfare are being addressed, consistent with the requirements of the law. However, unless there is an ongoing safety risk to you or to the Furman community, you will determine whether the university initiates any formal process. You are entitled to supportive measures (such as a no contact order or academic accommodations) regardless of whether you decide to initiate a formal process.</p>'
  '<p>Additional information about Furman&rsquo;s Sexual Misconduct Policy, how to report sexual misconduct, and your rights can be found at the Furman Title IX webpage at <a href="https://www.furman.edu/titleix">www.furman.edu/titleix</a>. You do not have to go through the experience alone.</p>')

ai_policy = item("Use of Generative Artificial Intelligence (AI)",
  '<p>This is a &ldquo;No, But&rdquo; course. This means that generative AI tools are <strong>generally prohibited</strong> unless explicitly permitted for specific assignments or activities.</p>'
  '<ul>'
  '<li>AI tools cannot be used to generate anything, in part or in whole, that is submitted with a student&rsquo;s name on it for credit, unless the instructor explicitly permits it for an assignment.</li>'
  '<li>Specific assignments may incorporate AI tools for specific learning objectives.</li>'
  '<li>When AI use is allowed, assignment instructions will identify which tools are allowed and to what extent they may be used.</li>'
  '<li>In cases of uncertainty, students should assume that no AI tool is allowed.</li>'
  '</ul>'
  '<p><strong>When AI is NOT Permitted:</strong> Generative AI tools that write text for you (such as ChatGPT, Microsoft Copilot, and Canva) are prohibited for these assignments. Violations will be considered academic misconduct.</p>'
  '<p><strong>When AI IS Permitted:</strong> If AI use is permitted for a specific assignment or activity, it will be clearly stated in the assignment or activity instructions. These instructions will specify:</p>'
  '<ul><li>What AI tools you may use</li><li>How you may use them</li><li>How you must acknowledge your use</li></ul>'
  '<p>Even when AI is permitted:</p>'
  '<ul>'
  '<li>You are responsible for verifying the accuracy of any AI-generated content</li>'
  '<li>You must acknowledge your use of AI as instructed</li>'
  '<li>You cannot upload copyrighted materials (textbooks, instructor notes, slides) to AI without express permission</li>'
  '</ul>'
  '<p><strong>Grammar and Spell Check Tools:</strong></p>'
  '<ul>'
  '<li>You may use your word processor&rsquo;s native spelling and grammar checker (e.g., built-in tools in Word or Google Docs that are not LLM-based) only to identify sentence-level issues. Allowing these tools to rewrite parts of sentences, whole sentences, or paragraphs is not acceptable. You do not need to cite the use of these standard tools.</li>'
  '<li>You may not use Grammarly or similar third-party writing assistants, as these tools often provide more intervention than is appropriate for this course.</li>'
  '</ul>'
  '<p><strong>When in Doubt, Ask!</strong> If you are uncertain whether AI use is permitted for a specific assignment or activity, ask me before you use it. If you have questions about what constitutes plagiarism or academic misconduct, consult me before it&rsquo;s too late! The penalty for academic integrity violations is an F for the assignment or, in case of multiple violations, an F for the course.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    <div class="sec-title" id="policies">Course Policies</div>
    <div class="sec-kicker">Please read these carefully &mdash; they explain how the class runs day to day.</div>
    {accessibility}
    {absences}
    {recordings}
    {nondiscrim}
  </div>
</div>
""")

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {integrity}
    {ai_policy}
  </div>
</div>
""")

# ---------------- RUBRICS ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.18in;">
    <div class="sec-title" id="rubrics" style="font-size:22px;">Engagement &amp; RRJ Rubrics</div>
    <div class="sec-kicker" style="margin-bottom:0.1in;">General rubrics that apply across the semester. A rubric for the Bhikkuni Ordination Game reflection paper will be added here once finalized.</div>
    <h4 class="block-title" style="margin-bottom:0.06in;">Engagement Rubric</h4>
    <p class="prose" style="font-size:10.5px; margin:0 0 0.08in;">Each class, your engagement will be assessed using the following scale:</p>
    <div class="cols3" style="font-size:10px;">
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">A-level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Fully engaged in all in-class activities;</li>
          <li>Fully attentive when others are speaking; and</li>
          <li>Fully attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">B-level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Mostly prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Mostly focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Mostly engaged in all in-class activities;</li>
          <li>Mostly attentive when others are speaking; and</li>
          <li>Mostly attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">C&ndash;D level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Arrived more than 5 minutes late and/or left before the end of class;</li>
          <li>Not prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Not prepared with some or any required assignments;</li>
          <li>Not focused on classroom discussions and activities (i.e., using technology in ways other than for use in classroom discussion or activities, conducting side conversations, engaging in behaviors that disrupt the focus of others);</li>
          <li>Not engaged in all in-class activities;</li>
          <li>Not attentive when others are speaking; OR</li>
          <li>Not attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>Not giving others the space and time to contribute;</li>
              <li>Not understanding that others come to our classroom with different experiences than your own; and</li>
              <li>Not being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <h4 class="block-title" style="margin-top:0.12in;">Reading and Reflection Journal (RRJ) Rubric</h4>
    <table class="weights">
      <thead><tr><th>Element</th><th>Aspects</th><th class="num">Points</th></tr></thead>
      <tbody>
        <tr><td>1. Comprehension</td><td>Demonstrates clear understanding of the assigned readings; accurately represents key concepts and ideas</td><td class="num">0&ndash;2</td></tr>
        <tr><td>2. Analysis</td><td>Goes beyond summary to provide insightful analysis; applies relevant analytical frameworks when appropriate</td><td class="num">0&ndash;2</td></tr>
        <tr><td>3. Depth of Reflection</td><td>Engages in meaningful personal reflection; connects ideas to own experiences or perspectives</td><td class="num">0&ndash;1</td></tr>
        <tr><td>4. Creativity</td><td>Responds imaginatively to creative prompts; demonstrates original thinking</td><td class="num">0&ndash;1</td></tr>
        <tr><td>5. Critical Thinking</td><td>Evaluates ideas critically; considers multiple perspectives</td><td class="num">0&ndash;1</td></tr>
        <tr><td>6. Connection-Making</td><td>Links concepts across different readings or topics; identifies broader implications or applications</td><td class="num">0&ndash;1</td></tr>
        <tr><td>7. Intellectual Curiosity</td><td>Raises thought-provoking questions; explores ideas beyond the immediate scope of the prompt</td><td class="num">0&ndash;1</td></tr>
        <tr><td>8. Evidence of Preparation</td><td>References specific details from assigned readings; shows thorough engagement with course materials</td><td class="num">0&ndash;1</td></tr>
        <tr><td><strong>Total</strong></td><td></td><td class="num"><strong>/10</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>
""")

with open(OUT, "w") as f:
    f.write(HEAD)
    f.write("\n".join(pages))
    f.write("</body></html>")

print("wrote", OUT, "pages so far:", len(pages))
