# 🚀 AI-Powered Cold Email Generator for Recruitment Outreach

## 📌 Project Overview
This project is an **AI-powered Cold Email Generator** designed for **recruitment and staffing companies**.  
The system requires **only a job posting URL as input** and automatically generates a **personalized cold email** to client companies, offering recruitment services for the specified role.

The generated email includes:
- Job-specific hiring pitch extracted from the job URL
- Relevant **candidate portfolio links**
- Professional recruitment-focused tone
- Clear call-to-action

---

## 🎯 Problem Statement
Recruitment companies manually analyze job postings and draft outreach emails, which is time-consuming and inconsistent.  
This project automates the entire workflow by **scraping job data directly from the job URL** and using **LLMs + vector databases** to generate high-quality cold emails.

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **LLM Model:** LLaMA (via Groq API)  
- **Frameworks & Libraries:**
  - LangChain
  - Streamlit
  - ChromaDB
  - Web Scraping (BeautifulSoup / Requests)
- **Development Environment:** PyCharm  

---

## ⚙️ System Workflow
1. User provides **only the Job Posting URL**
2. Job description is **web-scraped automatically**
3. Key job requirements and role details are extracted
4. Relevant portfolio data is retrieved using **ChromaDB**
5. **LangChain Prompt Templates** structure the email
6. **LLaMA (via Groq API)** generates a personalized cold email
7. Final email is displayed via **Streamlit UI**

---

## 🧠 Key Concepts Used
- Web Scraping & Content Extraction
- Prompt Engineering
- LangChain Chains
- Vector Embeddings & Semantic Search
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- LLM-based Text Generation

---

## ✨ Features
- Single-input system (Job URL only)
- Automatic job requirement extraction
- Portfolio-to-role matching
- AI-generated professional emails
- Fast inference using Groq API
- Clean Streamlit interface

---

## 📌 Use Cases
- Recruitment & Staffing Agencies
- HR Consultancies
- Talent Acquisition Teams
- B2B Hiring Outreach Automation

---

## 🚀 Future Enhancements
- Support for multiple job portals
- Email tone customization
- Automated email sending
- Candidate availability matching

---

## 📄 License
This project is for educational and learning purposes.
