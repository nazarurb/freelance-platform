--
-- PostgreSQL database dump
--

-- Dumped from database version 16.7 (Homebrew)
-- Dumped by pg_dump version 16.7 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin_actions; Type: TABLE; Schema: public; Owner: melnyk
--

CREATE TABLE public.admin_actions (
    id integer NOT NULL,
    admin_id integer NOT NULL,
    action character varying(255) NOT NULL,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.admin_actions OWNER TO melnyk;

--
-- Name: admin_actions_id_seq; Type: SEQUENCE; Schema: public; Owner: melnyk
--

CREATE SEQUENCE public.admin_actions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.admin_actions_id_seq OWNER TO melnyk;

--
-- Name: admin_actions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: melnyk
--

ALTER SEQUENCE public.admin_actions_id_seq OWNED BY public.admin_actions.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: melnyk
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO melnyk;

--
-- Name: permissions; Type: TABLE; Schema: public; Owner: melnyk
--

CREATE TABLE public.permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    granted_at timestamp without time zone NOT NULL
);


ALTER TABLE public.permissions OWNER TO melnyk;

--
-- Name: permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: melnyk
--

CREATE SEQUENCE public.permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.permissions_id_seq OWNER TO melnyk;

--
-- Name: permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: melnyk
--

ALTER SEQUENCE public.permissions_id_seq OWNED BY public.permissions.id;


--
-- Name: requests; Type: TABLE; Schema: public; Owner: melnyk
--

CREATE TABLE public.requests (
    id integer NOT NULL,
    user_id integer NOT NULL,
    description text NOT NULL,
    price_suggestion integer,
    status character varying(50),
    created_at timestamp without time zone,
    title character varying(100) NOT NULL,
    blocked_until timestamp without time zone
);


ALTER TABLE public.requests OWNER TO melnyk;

--
-- Name: requests_id_seq; Type: SEQUENCE; Schema: public; Owner: melnyk
--

CREATE SEQUENCE public.requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.requests_id_seq OWNER TO melnyk;

--
-- Name: requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: melnyk
--

ALTER SEQUENCE public.requests_id_seq OWNED BY public.requests.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: melnyk
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password_hash character varying NOT NULL,
    role character varying,
    blocked_until timestamp without time zone,
    created_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO melnyk;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: melnyk
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO melnyk;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: melnyk
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: admin_actions id; Type: DEFAULT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.admin_actions ALTER COLUMN id SET DEFAULT nextval('public.admin_actions_id_seq'::regclass);


--
-- Name: permissions id; Type: DEFAULT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.permissions ALTER COLUMN id SET DEFAULT nextval('public.permissions_id_seq'::regclass);


--
-- Name: requests id; Type: DEFAULT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.requests ALTER COLUMN id SET DEFAULT nextval('public.requests_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: admin_actions; Type: TABLE DATA; Schema: public; Owner: melnyk
--

COPY public.admin_actions (id, admin_id, action, "timestamp") FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: melnyk
--

COPY public.alembic_version (version_num) FROM stdin;
9b8c356c0283
\.


--
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: melnyk
--

COPY public.permissions (id, user_id, granted_at) FROM stdin;
2	13	2025-02-18 09:43:32.971301
\.


--
-- Data for Name: requests; Type: TABLE DATA; Schema: public; Owner: melnyk
--

COPY public.requests (id, user_id, description, price_suggestion, status, created_at, title, blocked_until) FROM stdin;
2	6	Job Title: Full Stack DeveloperWe are seeking a talented and experienced Fullstack Developer to join our development team and play a crucial role in designing, building, and maintaining our applications. If you are passionate about web development, possess a strong skill set in front end and backend technologies, and are eager to work on complex projects, we want to hear from you.Responsibilities:- Develop and maintain front end and backend components of our multitenant applications.- Create and manage APIs for seamless data communication between various application modules.- Work with NoSQL databases, including MongoDB, to store and retrieve data efficiently.- Utilize Node.js, JavaScript, and CSS to create responsive and interactive user interfaces.- Collaborate with the team to implement features using Angular, Express.js, and Ember.js.- Incorporate REST and GraphQL APIs to enhance application functionality.- Manage code repositories on GitHub and ensure proper version control.- Write clean, efficient, and maintainable code that adheres to best practices.- Troubleshoot and resolve software defects and issues as they arise.Optimize application performance and scalability.- Stay up-to-date with emerging technologies and industry trends to continually enhance your skills.Requirements:- Proven experience as a Fullstack Developer or similar role.- Proficiency in front end technologies such as Angular, JavaScript, CSS, and HTML.- Strong knowledge of backend technologies, including Node.js and Express.js.- Experience with NoSQL databases like MongoDB.- Familiarity with multitenant application architecture and development.- Solid understanding of REST and GraphQL API concepts.- Previous experience with CodePen for rapid prototyping is a plus.- Strong version control skills using GitHub.- Excellent problem-solving and debugging skills.- Knowledge of SQL and relational databases is a bonus.- Ability to work collaboratively in a team environment and independently when required.The project at hand is of moderate scale and expected to last approximately 1 to 2 months. We are specifically seeking an intermediate-level expert who can offer dependable solutions and deliver exceptional work within the specified timeframe.Budget: $1,100Posted On: February 17, 2024 09:09 UTCCategory: Full Stack DevelopmentSkills:AngularJS,     MongoDB,     NGINX,     SQLite,     JavaScript,     Web Development,     React,     Node.js,     Web Application,     APISkills:        AngularJS,                     MongoDB,                     NGINX,                     SQLite,                     JavaScript,                     Web Development,                     React,                     Node.js,                     Web Application,                     APICountry: United Statesclick to apply	1100	open	2025-02-16 19:44:24.896335	Full Stack Developer	\N
3	6	We are looking for a resource who can work part-time for one of our projects. The work time is around 8:30 pm IST (we need 4-5 hours of support per day) Monday-Friday.* You will be required to work via Zoom call* Mandatory 2-3 years of experience in Data Engineering technique is mandatory* We need the resource to work in the Indian time around 8:30 pm IST onwards* Design, develop, and maintain ETL processes using Python and SQL to ensure accurate and timely data extraction, transformation, and loading into data warehouses or lakes.* For creating pipelines Apache Dagster is the tool currently being used.* Create and manage data pipelines for efficient data movement and transformation using tools such as Apache Iceberg, Apache Trino, and AWS services.* Work closely with data analysts and data scientists to understand data requirements and design efficient data models and data structures for analytics and reporting purposes.* Monitor and troubleshoot data pipelines to ensure the integrity and consistency of data.* Optimize and tune database queries and data processing algorithms to improve performance and reduce latency.* Develop and maintain data documentation and data quality standards to ensure the accuracy and consistency of data.* Stay up-to-date with the latest data engineering technologies and trends, and proactively recommend changes and improvements to existing systems and processes.* Collaborate with cross-functional teams including software engineers, product managers, and business stakeholders to ensure the successful delivery of data-driven projects.* Strong Skills with experience in SQL, Python &amp; and Git are mandatory.* Should be available for the hours mentioned.Budget: $650Posted On: February 17, 2024 09:07 UTCCategory: Data EngineeringSkills:Docker,     ETL Pipeline,     Python,     SQL,     Amazon Web Services,     Git,     GitLabSkills:        Docker,                     ETL Pipeline,                     Python,                     SQL,                     Amazon Web Services,                     Git,                     GitLabCountry: Indiaclick to apply	650	open	2025-03-16 19:53:51.336606	Data Engineer	\N
6	6	Full stack developer to build a website using php and ph frameworks. Posted On: February 17, 2024 08:56 UTCCategory: Full Stack DevelopmentSkills:Web Development,     HTML,     Web Application,     PHP,     JavaScriptSkills:        Web Development,                     HTML,                     Web Application,                     PHP,                     JavaScriptCountry: Indiaclick to apply	850	open	2025-02-16 19:58:08.526908	Full Stack Developer	\N
10	6	I am Looking for freelancers specializing in web development or Data Analytics . Don't have any ratings or struggling with a bad rating? I can work with you.I offer a unique opportunity that requires just 5 minutes of your time. In return, I'll provide you with $5 and a guaranteed 5-star feedback, complete with detailed positive comments to enhance your profile once the task is completed.RequirementsMust have 2 year old google account to access docMust be residing in Seattle or surround areasBudget: $5Posted On: February 16, 2024 22:32 UTCCategory: Data AnalyticsSkills:Data Entry,     Data AnalysisSkills:        Data Entry,                     Data AnalysisCountry: Costa Ricaclick to apply	450	open	2025-02-16 20:00:46.282643	Data Engineer	\N
11	6	Hi. I am based in Vadodara India and I am looking for someone from Vadodara itself. I am owner of Handmade Jewellery Business and I am looking for someone who can manage my Social Media. Create posts with good captions, Proper hashtags to increase my followers and tap potential customers.My budget is 70 to 80 Rs per post. If this suits anyone's requirement, kindly DM me with your details.Budget: $30Posted On: February 18, 2024 09:10 UTCCategory: Social Media MarketingSkills:Social Media Marketing,     Facebook,     Social Media Management,     Instagram,     Social Media Content Creation,     Instagram Story,     Social Media ContentSkills:        Social Media Marketing,                     Facebook,                     Social Media Management,                     Instagram,                     Social Media Content Creation,                     Instagram Story,                     Social Media ContentCountry: Indiaclick to apply	30	open	2025-02-16 20:04:07.609987	Social Media Makerting	\N
9	6	We are looking for a freelancer to grow into a full-time team member.  The ideal candidate will read this description and will reply to this posting with their interest.We have a UX/UI designer who will create a website in Figma for client approval.  You will take that approved design and recreate it exactly in Wordpress using Divi.  You will optimize for speed and mobile responsiveness as you design.  Our websites are standard 7-page marketing websites for local small businesses.  Please read the job description before you inform us of your interest.  This is an entry-level position, it's okay if you need some training.  You either need to speak English or Bulgarian.Hourly Range: $4.00-$6.00Posted On: February 16, 2024 22:34 UTCCategory: CMS DevelopmentSkills:Divi,     Website,     Landing Page,     Plugin Customization,     PSD to WordPress,     WordPressSkills:        Divi,                     Website,                     Landing Page,                     Plugin Customization,                     PSD to WordPress,                     WordPressCountry: United Statesclick to apply	300	open	2025-01-16 19:59:57.995081	Junior Web Developer	\N
12	6	looking for someone good in sending ads in whtsapp groups, forums and other useful groupsBudget: $20Posted On: February 18, 2024 10:44 UTCCategory: Lead GenerationSkills:Sales & Marketing,     Social Media Marketing,     Lead Generation,     Email Marketing,     Internet MarketingSkills:        Sales & Marketing,                     Social Media Marketing,                     Lead Generation,                     Email Marketing,                     Internet MarketingCountry: Indiaclick to apply	20	open	2025-03-16 20:05:01.936169	Marketing leads	\N
1	6	We are looking for a skilled Python Backend Developer to join our team. You will be responsible for building and maintaining scalable APIs, optimizing database performance, and ensuring the reliability of backend services.	500	open	2025-01-16 19:29:21.32539	Python Backend developer	\N
5	6	We are looking for a Web3 full-stack developer to develop our Dapp in EVM-compatible chains. You'll need to build the whole Dapp with us, starting from scratch.Requirements:- good English spoken and written level- familiar with Solidity, hardhat/foundry- expert on Next.js, React.js and Node.js- have experience on integration with popular wallet like Metamask, OKX wallet, etc- Figma UI/UX recommended.Hourly Range: $30.00-$50.00Posted On: February 17, 2024 09:04 UTCCategory: Full Stack DevelopmentSkills:Next.js,     Web Application,     JavaScript,     CSS,     React,     Solidity,     Node.js,     EthereumSkills:        Next.js,                     Web Application,                     JavaScript,                     CSS,                     React,                     Solidity,                     Node.js,                     EthereumCountry: Malaysiaclick to apply	750	open	2025-01-16 19:57:03.67345	Web3 Full-stack Developer	\N
7	6	Web Developer Specializing in HTML, CSS, JavaScript, and UnbounceJob Description:The Web Developer will need to migrate our web pages from Shopify to Unbounce. The responsibilities will include the technical aspects of transferring pages, managing domain reassignments, and contributing to the maintenance and development of new pages on Unbounce. This role requires a blend of technical proficiency, creativity, and a keen eye for detail to ensure our digital assets are optimized, compliant, and aligned with our brand's vision.Key Responsibilities:- Lead the migration of existing web pages from Shopify to - Unbounce, ensuring a smooth and efficient transition.- Manage the reassignment of domains to the newly migrated pages on Unbounce, ensuring seamless access and functionality.- Conduct regular maintenance of pages hosted on Unbounce, addressing any issues and implementing updates as needed.- Develop new pages on Unbounce, from concept to deployment, in collaboration with our marketing team to support ongoing campaigns and initiatives.- Optimize pages for performance, SEO, and compliance with web standards.- Collaborate with team members to ensure consistency and coherence across our digital assets.- Stay up-to-date with the latest web development technologies and best practices, suggesting and implementing improvements to our web infrastructure.Posted On: February 16, 2024 22:35 UTCCategory: Full Stack DevelopmentSkills:HTML,     CSS,     JavaScript,     Landing Page,     Website,     Web Development,     HTML5,     CSS 3Skills:        HTML,                     CSS,                     JavaScript,                     Landing Page,                     Website,                     Web Development,                     HTML5,                     CSS 3Country: United Statesclick to apply	750	open	2025-03-16 19:59:06.215073	Web Developer	\N
13	6	We're on the lookout for a talented Fullstack Developer to join our team. As a Fullstack Developer, you'll be involved in both frontend and backend development, tackling a variety of challenges across the entire application stack.Responsibilities:- Develop robust and scalable web applications, handling both frontend and backend tasks.- Collaborate with the design and product teams to implement features and functionalities.- Write clean, maintainable, and efficient code for both frontend and backend components.- Implement responsive and user-friendly interfaces using modern frontend technologies.- Design and develop RESTful APIs for seamless communication between frontend and backend systems.Requirements:- Proven experience as a Fullstack Developer or similar role.- Proficiency in frontend technologies such as HTML, CSS, JavaScript, and frameworks like React.js.- Experience with databases like MongoDB, MySQL..- Familiarity with version control systems such as Git.- Good problem-solving skills and attention to detail.- Ability to work collaboratively in a team environment.If you're passionate about building end-to-end web applications and possess the necessary skills, we'd love to hear from you. Please share examples of your work and your availability for this role.Budget: $100Posted On: February 17, 2024 16:00 UTCCategory: Full Stack DevelopmentSkills:JavaScript,     Node.js,     API,     MongoDB,     CSS,     MySQL,     Web Development,     Database Architecture,     API IntegrationSkills:        JavaScript,                     Node.js,                     API,                     MongoDB,                     CSS,                     MySQL,                     Web Development,                     Database Architecture,                     API IntegrationCountry: United Statesclick to apply	750	open	2025-03-15 20:05:41.498903	Full Stack Developer	\N
8	6	Web Developer Specializing in HTML, CSS, JavaScript, and UnbounceJob Description:The Web Developer will need to migrate our web pages from Shopify to Unbounce. The responsibilities will include the technical aspects of transferring pages, managing domain reassignments, and contributing to the maintenance and development of new pages on Unbounce. This role requires a blend of technical proficiency, creativity, and a keen eye for detail to ensure our digital assets are optimized, compliant, and aligned with our brand's vision.Key Responsibilities:- Lead the migration of existing web pages from Shopify to - Unbounce, ensuring a smooth and efficient transition.- Manage the reassignment of domains to the newly migrated pages on Unbounce, ensuring seamless access and functionality.- Conduct regular maintenance of pages hosted on Unbounce, addressing any issues and implementing updates as needed.- Develop new pages on Unbounce, from concept to deployment, in collaboration with our marketing team to support ongoing campaigns and initiatives.- Optimize pages for performance, SEO, and compliance with web standards.- Collaborate with team members to ensure consistency and coherence across our digital assets.- Stay up-to-date with the latest web development technologies and best practices, suggesting and implementing improvements to our web infrastructure.Posted On: February 16, 2024 22:35 UTCCategory: Full Stack DevelopmentSkills:HTML,     CSS,     JavaScript,     Landing Page,     Website,     Web Development,     HTML5,     CSS 3Skills:        HTML,                     CSS,                     JavaScript,                     Landing Page,                     Website,                     Web Development,                     HTML5,                     CSS 3Country: United Statesclick to apply	750	open	2025-02-16 19:59:11.965543	Web Developer	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: melnyk
--

COPY public.users (id, username, email, password_hash, role, blocked_until, created_at) FROM stdin;
2	anna_user	anna.user@example.com	$2b$12$i4w7IcFSKnhjRkBV6cqniuSpMadDz38mcLfZz2pY06VhJdv41YPqa	user	\N	2025-02-16 16:39:25.464016
3	mike_smith	mike.admin@example.com	$2b$12$iz1.GtdhlmEeNCpHwr1JGuBkcfrnMWlw3mY9IDrtyi6fx0rtw58Wm	admin	\N	2025-02-16 16:42:31.472985
6	will_smith	will.smith@example.com	$2b$12$IpYlLpyIETIF5zMeAbYCGOCvbN3kMjvBassHxeCzRrdfSsjvMMu7e	user	\N	2025-02-16 18:07:58.079157
5	john_doe	john.doe@example.com	$2b$12$3hyG04LoKdDvTa2xmY6JsORYnLs.YksopKzO6T1BzprE1Q3PeWFKm	admin	\N	2025-02-16 16:43:20.769112
7	admin_user	admin@example.com	$2b$12$AS8ozF9M3Nl.KrLo.JOFKOXVUtfnJMM38QlxG5cCMPQ8hesihh2Bi	admin	\N	2025-02-17 19:15:58.409281
13	emma_developer	emma.dev@example.com	$2b$12$FTMxaNWr4eylj1Igs9tR6uSzA5UUOf6.uryWPem.HpXtqz4/Y.6oK	admin	\N	2025-02-18 07:10:41.873861
4	katya_testings	katya.tests@example.com	$2b$12$pApL/9OzMAjuK2ZGrn5sGOXcZJbGFF0NtytmoS.5d8obm7Eijc00m	user	\N	2025-02-16 16:42:57.491876
8	john_johns	john.johns@example.com	$2b$12$QsYK6yOsmgB225DMRF2w6uC.Mdt2BWq.EjzXYIhSW6K8.J/BCcDQO	user	\N	2025-02-17 20:27:15.820055
\.


--
-- Name: admin_actions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: melnyk
--

SELECT pg_catalog.setval('public.admin_actions_id_seq', 1, false);


--
-- Name: permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: melnyk
--

SELECT pg_catalog.setval('public.permissions_id_seq', 2, true);


--
-- Name: requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: melnyk
--

SELECT pg_catalog.setval('public.requests_id_seq', 18, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: melnyk
--

SELECT pg_catalog.setval('public.users_id_seq', 15, true);


--
-- Name: admin_actions admin_actions_pkey; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.admin_actions
    ADD CONSTRAINT admin_actions_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: permissions permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);


--
-- Name: permissions permissions_user_id_key; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_user_id_key UNIQUE (user_id);


--
-- Name: requests requests_pkey; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.requests
    ADD CONSTRAINT requests_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: admin_actions admin_actions_admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.admin_actions
    ADD CONSTRAINT admin_actions_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.users(id);


--
-- Name: permissions permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: requests requests_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: melnyk
--

ALTER TABLE ONLY public.requests
    ADD CONSTRAINT requests_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

