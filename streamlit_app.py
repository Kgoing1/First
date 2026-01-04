import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Initialize session state for storing projects
if 'milestone_projects' not in st.session_state:
    st.session_state.milestone_projects = []

if 'small_projects' not in st.session_state:
    st.session_state.small_projects = []

if 'timeline_events' not in st.session_state:
    st.session_state.timeline_events = []

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #1f77b4;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #ff7f0e;
    }
    .project-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #1f77b4;
    }
    .timeline-item {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #2ca02c;
    }
    .timeline-date {
        font-weight: bold;
        color: #2ca02c;
    }
    .form-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">🚀 My Portfolio</div>', unsafe_allow_html=True)

# About section
st.markdown('<div class="section-header">👋 About Me</div>', unsafe_allow_html=True)
st.write("""
Welcome to my portfolio! I'm a passionate developer/learning enthusiast who loves creating innovative solutions.
This website showcases my journey through milestone projects, smaller experiments, and my learning timeline.
""")

# Milestone Projects section
st.markdown('<div class="section-header">🏆 Milestone Projects</div>', unsafe_allow_html=True)

# Form to add milestone projects
with st.expander("➕ Add Milestone Project"):
    with st.form("milestone_form"):
        title = st.text_input("Project Title")
        description = st.text_area("Project Description")
        technologies = st.text_input("Technologies (comma-separated)")
        link = st.text_input("Project Link")
        image = st.text_input("Image URL")
        submitted = st.form_submit_button("Add Project")

        if submitted and title:
            new_project = {
                "title": title,
                "description": description,
                "technologies": [tech.strip() for tech in technologies.split(',') if tech.strip()],
                "link": link,
                "image": image or "https://via.placeholder.com/300x200?text=No+Image"
            }
            st.session_state.milestone_projects.append(new_project)
            st.success("Project added successfully!")

# Display milestone projects
if st.session_state.milestone_projects:
    cols = st.columns(3)
    for i, project in enumerate(st.session_state.milestone_projects):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <img src="{project['image']}" style="width:100%; border-radius:5px;">
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {', '.join(project['technologies'])}</p>
                {"<a href='" + project['link'] + "' target='_blank'>View Project</a>" if project['link'] else ""}
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("No milestone projects added yet. Use the form above to add your first project!")

# Small Projects section
st.markdown('<div class="section-header">🔧 Small Projects</div>', unsafe_allow_html=True)

# Form to add small projects
with st.expander("➕ Add Small Project"):
    with st.form("small_form"):
        title = st.text_input("Project Title", key="small_title")
        description = st.text_area("Project Description", key="small_desc")
        technologies = st.text_input("Technologies (comma-separated)", key="small_tech")
        link = st.text_input("Project Link", key="small_link")
        submitted = st.form_submit_button("Add Project", key="small_submit")

        if submitted and title:
            new_project = {
                "title": title,
                "description": description,
                "technologies": [tech.strip() for tech in technologies.split(',') if tech.strip()],
                "link": link
            }
            st.session_state.small_projects.append(new_project)
            st.success("Project added successfully!")

# Display small projects
if st.session_state.small_projects:
    cols = st.columns(2)
    for i, project in enumerate(st.session_state.small_projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="project-card">
                <h4>{project['title']}</h4>
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {', '.join(project['technologies'])}</p>
                {"<a href='" + project['link'] + "' target='_blank'>View Code</a>" if project['link'] else ""}
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("No small projects added yet. Use the form above to add your first project!")

# Learning Timeline section
st.markdown('<div class="section-header">📚 Learning Timeline</div>', unsafe_allow_html=True)

# Form to add timeline events
with st.expander("➕ Add Timeline Event"):
    with st.form("timeline_form"):
        date = st.date_input("Event Date")
        title = st.text_input("Event Title", key="timeline_title")
        description = st.text_area("Event Description", key="timeline_desc")
        submitted = st.form_submit_button("Add Event", key="timeline_submit")

        if submitted and title:
            new_event = {
                "date": date.strftime('%Y-%m-%d'),
                "title": title,
                "description": description
            }
            st.session_state.timeline_events.append(new_event)
            st.success("Event added successfully!")

# Display timeline events (sorted by date, most recent first)
if st.session_state.timeline_events:
    # Sort events by date
    sorted_events = sorted(st.session_state.timeline_events, key=lambda x: x['date'], reverse=True)
    for event in sorted_events:
        date_obj = datetime.strptime(event['date'], '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %Y')
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-date">{formatted_date}</div>
            <h4>{event['title']}</h4>
            <p>{event['description']}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No timeline events added yet. Use the form above to add your first learning milestone!")

# Footer
st.markdown("---")
st.markdown("### 📞 Contact Me")
st.write("Feel free to reach out for collaborations or opportunities!")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("📧 Email: your.email@example.com")
with col2:
    st.write("💼 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)")
with col3:
    st.write("🐙 GitHub: [Your GitHub](https://github.com/yourusername)")
