
import streamlit as st
from pypdf import PdfReader

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config( 
    page_title="AI Resume & Job Matching Agent",
    page_icon="🤖"
)

st.title("🤖 AI Resume & Job Matching Agent")

st.write(
    "Upload your resume and enter a job description "
    "to analyze your job match."
)

# -----------------------------
# SKILLS
# -----------------------------

skills = [
    "python",
    "machine learning",
    "sql",
    "data analysis",
    "pandas",
    "scikit-learn",
    "power bi",
    "html",
    "css"
]

# -----------------------------
# RESUME AGENT
# -----------------------------

def resume_agent(resume_text):

    resume_skills = []
    resume_lower = resume_text.lower()

    for skill in skills:
        if skill in resume_lower:
            resume_skills.append(skill)

    return resume_skills


# -----------------------------
# JOB AGENT
# -----------------------------

def job_agent(job_description):

    required_skills = []
    job_lower = job_description.lower()

    for skill in skills:
        if skill in job_lower:
            required_skills.append(skill)

    return required_skills


# -----------------------------
# MATCH AGENT
# -----------------------------

def match_agent(resume_skills, required_skills):

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if required_skills:
        match_score = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_score = 0

    return matched_skills, missing_skills, match_score


# -----------------------------
# RECOMMENDATION AGENT
# -----------------------------

def recommendation_agent(match_score, missing_skills):

    if match_score >= 80:
        return "🌟 Excellent match! Your resume fits this job very well."

    elif match_score >= 50:
        return "👍 Good match! Improve the missing skills to increase your chances."

    else:
        return "⚠️ Low match. Consider developing more of the required skills."


# -----------------------------
# USER INTERFACE
# -----------------------------

st.subheader("📄 Upload Resume")

resume_file = st.file_uploader(
    "Choose your resume PDF",
    type=["pdf"]
)

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200
)

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

if st.button("🔍 Analyze Resume"):

    if resume_file is None:

        st.warning("Please upload your resume.")

    elif job_description.strip() == "":

        st.warning("Please enter a job description.")

    else:

        # Read PDF
        reader = PdfReader(resume_file)

        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() or ""

        # Check whether PDF contains text
        if not resume_text.strip():

            st.error(
                "⚠️ This PDF does not contain selectable text. "
                "Please use a text-based PDF resume for now."
            )

        else:

            # Run agents
            resume_skills = resume_agent(resume_text)

            required_skills = job_agent(job_description)

            matched_skills, missing_skills, match_score = match_agent(
                resume_skills,
                required_skills
            )

            recommendation = recommendation_agent(
                match_score,
                missing_skills
            )

            # -----------------------------
            # RESULTS
            # -----------------------------

            st.divider()

            st.subheader("📊 Analysis Result")

            st.metric(
                "Resume Match Score",
                f"{match_score:.0f}%"
            )

            st.subheader("✅ Matched Skills")

            if matched_skills:

                for skill in matched_skills:
                    st.write("✅", skill.title())

            else:

                st.write("No matching skills found.")

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.write("❌", skill.title())

            else:

                st.write("🎉 No missing skills!")

            st.subheader("💡 Recommendation")

            st.info(recommendation)
            
