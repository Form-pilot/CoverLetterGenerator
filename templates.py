latex_template = r"""\documentclass[11pt,a4paper,sans]{moderncv}

\moderncvstyle{classic}
\moderncvcolor{blue}

\usepackage[scale=0.75]{geometry}
\setlength{\footskip}{136.00005pt}

\ifxetexorluatex
  \usepackage{fontspec}
  \usepackage{unicode-math}
  \defaultfontfeatures{Ligatures=TeX}
  \setmainfont{Latin Modern Roman}
  \setsansfont{Latin Modern Sans}
  \setmonofont{Latin Modern Mono}
  \setmathfont{Latin Modern Math} 
\else
  \usepackage[T1]{fontenc}
  \usepackage{lmodern}
\fi

\usepackage[english]{babel}

\name{John}{Doe}
\title{Résumé title}
\born{4 July 1776}
\address{street and number}{postcode city}{country}
\phone[mobile]{+1~(234)~567~890}
\phone[fixed]{+2~(345)~678~901}
\phone[fax]{+3~(456)~789~012}
\email{john@doe.org}
\homepage{www.johndoe.com}

\social[linkedin]{john.doe}
\social[xing]{john\_doe}
\social[twitter]{ji\_doe}
\social[github]{jdoe}
\social[gitlab]{jdoe}

\extrainfo{additional information}
\quote{Some quote}

\renewcommand*{\bibliographyitemlabel}{[\arabic{enumiv}]}

\begin{document}

\makecvtitle

\section{Education}
\cventry{year--year}{Degree}{Institution}{City}{\textit{Grade}}{Description}
\cventry{year--year}{Degree}{Institution}{City}{\textit{Grade}}{Description}

\section{Master thesis}
\cvitem{title}{\emph{Title}}
\cvitem{supervisors}{Supervisors}
\cvitem{description}{Short thesis abstract}

\section{Experience}
\cventry{year--year}{Job title}{Employer}{City}{}{General description no longer than 1--2 lines.\newline{}
Detailed achievements:
\begin{itemize}
\item Achievement 1
\item Achievement 2 (with sub-achievements)
  \begin{itemize}
  \item Sub-achievement (a);
  \item Sub-achievement (b), with sub-sub-achievements;
    \begin{itemize}
    \item Sub-sub-achievement i;
    \item Sub-sub-achievement ii;
    \item Sub-sub-achievement iii;
    \end{itemize}
  \item Sub-achievement (c);
  \end{itemize}
\item Achievement 3
\item Achievement 4
\end{itemize}}
\cventry{year--year}{Job title}{Employer}{City}{}{Description line 1\newline{}Description line 2\newline{}Description line 3}
\subsection{Miscellaneous}
\cventry{year--year}{Job title}{Employer}{City}{}{Description}

\section{Languages}
\cvitemwithcomment{Language 1}{Skill level}{Comment}
\cvitemwithcomment{Language 2}{Skill level}{Comment}
\cvitemwithcomment{Language 3}{Skill level}{Comment}
\cvitemwithcomment{Language 4}{Skill level}{Comment}

\section{Computer skills}
\cvdoubleitem{category 1}{XXX, YYY, ZZZ}{category 4}{XXX, YYY, ZZZ}
\cvdoubleitem{category 2}{XXX, YYY, ZZZ}{category 5}{XXX, YYY, ZZZ}
\cvdoubleitem{category 3}{XXX, YYY, ZZZ}{category 6}{XXX, YYY, ZZZ}

\section{Skill matrix}
\cvitem{Skill matrix}{Alternatively, provide a skill matrix to show off your skills}

\cvskilllegend*[1em]{}

\cvskillhead[-0.1em]

\cvskillentry*{Language:}{3}{Python}{2}{I'm so experienced in Python and have realised a million projects. At least.}
\cvskillentry{}{2}{Lilypond}{14}{So much sheet music! Man, I'm the best!}
\cvskillentry{}{3}{\LaTeX}{14}{Clearly I rock at \LaTeX}
\cvskillentry*{OS:}{3}{Linux}{2}{I only use Archlinux btw}
\cvskillentry*[1em]{Methods}{4}{SCRUM}{8}{SCRUM master for 5 years}

\section{Interests}
\cvitem{hobby 1}{Description}
\cvitem{hobby 2}{Description}
\cvitem{hobby 3}{Description}

\section{Extra 1}
\cvlistitem{Item 1}
\cvlistitem{Item 2}
\cvlistitem{Item 3. This item is particularly long and therefore normally spans over several lines. Did you notice the indentation when the line wraps?}

\section{Extra 2}
\cvlistdoubleitem{Item 1}{Item 4}
\cvlistdoubleitem{Item 2}{Item 5\cite{book2}}
\cvlistdoubleitem{Item 3}{Item 6. Like item 3 in the single column list before, this item is particularly long to wrap over several lines.}

\section{References}
\begin{cvcolumns}
  \cvcolumn{Category 1}{\begin{itemize}\item Person 1\item Person 2\item Person 3\end{itemize}}
  \cvcolumn{Category 2}{Amongst others:\begin{itemize}\item Person 1, and\item Person 2\end{itemize}(more upon request)}
  \cvcolumn[0.5]{All the rest \& some more}{\textit{That} person, and \textbf{those} also (all available upon request).}
\end{cvcolumns}

\nocite{*}
\bibliographystyle{plain}
\bibliography{publications}

\end{document}"""

mohammad_resume = """
Mohammad
Mohammadi

Senior Software Engineer
Twickenham,
Greater London, UK
(+44)-77700-31702
m@mohammadi.com
mohammadi.com
Mohammadi-com
mohammadmohammadi
Global Talent Visa Holder

Experiences
Nov2022
May2024
Software Development Engineer, Amadeus, London, UK
Amadeus is a leading technology provider in the global travel industry, deliv-
ering cutting-edge solutions, technology, and services to a wide array of travel
providers, including airlines, hotels, and travel agencies. Contributions:
Played an integral role in the core team that facilitated the migration of
services from legacy systems to RESTful APIs.
Developed custom features for Southwest Airlines using C++
Successfully consolidated two highly coupled repositories, reducing pull re-
quests by 30% and significantly enhancing our team’s overall eﬀiciency.
Authored and executed regression tests using Pytest, ensuring the stability
and reliability of our codebase.
Enhanced system performance by integrating automated CI/CD pipelines
using Jenkins.
Utilized Jira and Bitbucket for eﬀicient task management and version control,
ensuring project alignment with agile methodologies.
Mentored and onboarded new team members, sharing knowledge and best
practices to enhance team performance.
Proposed and implemented a ”no meeting” policy for software engineers,
which received strong support from management and team members, result-
ing in a marked increase in productivity.

May2021
Nov2022
Full Stack Engineer & Co-Founder, Zumud, Tallinn, Estonia
Zumud was envisioned as a platform to redefine talent investment as an asset
class, enabling investors to receive a fixed percentage of future income from
talent over a specified term. Key achievements:
Successfully developed a Minimum Viable Product (MVP) that allowed in-
vestors to browse candidates and make investments.
Automated key business processes, including transaction handling and re-
porting, using Python scripts and third-party APIs.
Designed and implemented cloud-based solutions for eﬀicient data storage
and retrieval.
Ensured the reliability of the platform by implementing automated testing
frameworks.
Due to regulatory changes in the European Union, we ultimately decided not
to continue pursuing this idea.

Jan2018
Apr2021
Full Stack Engineer & Founding Partner, ParadiseHub Coworking
Space, Tehran, Iran
ParadiseHub stands as Iran’s leading and largest co-working space and digital
technology learning academy with 10 branches strategically located across the
country. Responsibilities:
Designed and implemented a scalable backend system for a web-based plat-
form similar to Airbnb for booking co-working spaces.
Managed a development team, emphasising code quality and scalability in
web application development.
Implemented cloud solutions to support the platform’s growing user base and
data needs.


Nov2016
Nov2017
Back-end Developer & Early Employee, Torob.com, Tehran, Iran
Torob is the dominant price comparison search engine in Iran. Key acheivments:
Developed and optimised backend systems using Django and Django REST
Framework, that is working with more than 5 million visits per month and
more than 20 million products.
Built and maintained RESTful APIs that powered the core features of the
price comparison engine.
Worked with Django ORM to read from Redis database as in-memory
database that used as a cache
Implemented and maintained a content delivery network (CDN) to improve
platform performance.
Worked on automated systems for data extraction and processing using
Scrapy framework.

Education
2013–2019 Bachelor’s Degree in Computer Engineering, Sharif University of
Technology, Tehran, Iran
Graduated top of my class from the leading IT Engineering program in Iran.

Computer Skills
Programming
Languages
Frameworks
& APIs
DevOps &
Tools
Python, C, C++, Java, SQL
Django, Django REST Framework, FastAPI, Flask, RESTful APIs
AWS, Docker, Jenkins, Git, Confluence, Jira, Bitbucket
Testing
Frameworks
PyTest, UnitTest, Automated Testing with Python
Backend PostgreSQL, MySQL, MongoDB, Redis
Certifications
2023 Certified SAFe® Practitioner

Honors & Awards
UK Global Talent Visa as a Recognised Leader in Digital Tech-
nology (Exceptional Talent), TechNation, London, UK
1st rank among B.Sc students of IT Engineering, Sharif University
of Technology, Tehran, Iran
Achieved the highest GPA among my peers.
Dec 2023 Sep 2019 
"""