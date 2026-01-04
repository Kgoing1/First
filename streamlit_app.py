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

# Custom CSS - Retro Macintosh Minimalistic Style
st.markdown("""
<style>
    * {
        font-family: 'Chicago', 'Monaco', monospace;
    }
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #000;
        font-family: 'Chicago', serif;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #000;
        font-family: 'Chicago', serif;
        border-bottom: 2px solid #000;
        padding-bottom: 0.5rem;
    }
    .project-card {
        background-color: #f0ede4;
        padding: 1rem;
        border-radius: 0px;
        margin-bottom: 1rem;
        border: 2px solid #000;
        font-size: 0.9rem;
    }
    .timeline-item {
        background-color: #f0ede4;
        padding: 1rem;
        border-radius: 0px;
        margin-bottom: 1rem;
        border: 2px solid #000;
        font-size: 0.9rem;
    }
    .timeline-date {
        font-weight: bold;
        color: #000;
        font-size: 0.85rem;
    }
    .form-container {
        background-color: #f0ede4;
        padding: 1rem;
        border-radius: 0px;
        margin-bottom: 1rem;
        border: 2px solid #000;
    }
    button {
        background-color: #f0ede4;
        border: 2px solid #000;
        padding: 0.3rem 0.8rem;
        font-family: 'Chicago', monospace;
        font-size: 0.85rem;
        cursor: pointer;
    }
    button:hover {
        background-color: #e8ddd0;
    }
    input, textarea, select {
        background-color: #fff;
        border: 2px solid #000;
        padding: 0.3rem;
        font-family: 'Chicago', monospace;
        font-size: 0.85rem;
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
st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)

# Form to add milestone projects
with st.expander("+ Add Project"):
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

# Fundamental Projects section
st.markdown('<div class="section-header">Fundamental Projects</div>', unsafe_allow_html=True)

# Form to add small projects
with st.expander("+ Add Fundamental Project"):
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
st.markdown('<div class="section-header">Learning Timeline</div>', unsafe_allow_html=True)

# Form to add timeline events
with st.expander("+ Add Timeline Event"):
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
    for idx, event in enumerate(sorted_events):
        date_obj = datetime.strptime(event['date'], '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %Y')
        
        col1, col2, col3 = st.columns([1, 0.15, 0.15])
        
        with col1:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-date">{formatted_date}</div>
                <h4>{event['title']}</h4>
                <p>{event['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("Edit", key=f"edit_{idx}"):
                st.session_state[f"editing_{idx}"] = True
        
        with col3:
            if st.button("Delete", key=f"delete_{idx}"):
                st.session_state.timeline_events.pop(sorted_events.index(event))
                st.rerun()
        
        # Edit form
        if st.session_state.get(f"editing_{idx}", False):
            with st.form(f"edit_timeline_form_{idx}"):
                new_date = st.date_input("Event Date", value=datetime.strptime(event['date'], '%Y-%m-%d').date(), key=f"edit_date_{idx}")
                new_title = st.text_input("Event Title", value=event['title'], key=f"edit_title_{idx}")
                new_description = st.text_area("Event Description", value=event['description'], key=f"edit_desc_{idx}")
                col_save, col_cancel = st.columns(2)
                
                with col_save:
                    if st.form_submit_button("Save Changes", key=f"save_edit_{idx}"):
                        # Find and update the event
                        for i, e in enumerate(st.session_state.timeline_events):
                            if e['date'] == event['date'] and e['title'] == event['title']:
                                st.session_state.timeline_events[i] = {
                                    "date": new_date.strftime('%Y-%m-%d'),
                                    "title": new_title,
                                    "description": new_description
                                }
                                break
                        st.session_state[f"editing_{idx}"] = False
                        st.success("Event updated!")
                        st.rerun()
                
                with col_cancel:
                    if st.form_submit_button("Cancel", key=f"cancel_edit_{idx}"):
                        st.session_state[f"editing_{idx}"] = False
                        st.rerun()
else:
    st.info("No timeline events added yet. Use the form above to add your first learning milestone!")

# Footer
st.markdown("---")
st.markdown("### Contact")
st.write("Reach out for collaborations or opportunities.")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Email: your.email@example.com")
with col2:
    st.write("LinkedIn: [Profile](https://linkedin.com/in/yourprofile)")
with col3:
    st.write("GitHub: [Profile](https://github.com/yourusername)")
