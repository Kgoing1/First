import streamlit as st
from datetime import datetime
import json
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Create data directory for persistent storage
DATA_DIR = Path("portfolio_data")
DATA_DIR.mkdir(exist_ok=True)

PHOTOS_DIR = DATA_DIR / "photos"
PHOTOS_DIR.mkdir(exist_ok=True)

# File paths for persistent storage
MILESTONE_PROJECTS_FILE = DATA_DIR / "milestone_projects.json"
SMALL_PROJECTS_FILE = DATA_DIR / "small_projects.json"
TIMELINE_EVENTS_FILE = DATA_DIR / "timeline_events.json"

# Load data from files
def load_milestone_projects():
    if MILESTONE_PROJECTS_FILE.exists():
        with open(MILESTONE_PROJECTS_FILE, 'r') as f:
            return json.load(f)
    return []

def load_small_projects():
    if SMALL_PROJECTS_FILE.exists():
        with open(SMALL_PROJECTS_FILE, 'r') as f:
            return json.load(f)
    return []

def load_timeline_events():
    if TIMELINE_EVENTS_FILE.exists():
        with open(TIMELINE_EVENTS_FILE, 'r') as f:
            return json.load(f)
    return []

def load_timeline_photos():
    """Load timeline photos from disk"""
    photos = {}
    if PHOTOS_DIR.exists():
        for photo_file in PHOTOS_DIR.glob("*"):
            if photo_file.is_file():
                with open(photo_file, 'rb') as f:
                    photos[photo_file.stem] = f.read()
    return photos

# Initialize session state with persistent data
if 'milestone_projects' not in st.session_state:
    st.session_state.milestone_projects = load_milestone_projects()

if 'small_projects' not in st.session_state:
    st.session_state.small_projects = load_small_projects()

if 'timeline_events' not in st.session_state:
    st.session_state.timeline_events = load_timeline_events()

if 'timeline_photos' not in st.session_state:
    st.session_state.timeline_photos = load_timeline_photos()

# Save functions
def save_milestone_projects():
    with open(MILESTONE_PROJECTS_FILE, 'w') as f:
        json.dump(st.session_state.milestone_projects, f, indent=2)

def save_small_projects():
    with open(SMALL_PROJECTS_FILE, 'w') as f:
        json.dump(st.session_state.small_projects, f, indent=2)

def save_timeline_events():
    with open(TIMELINE_EVENTS_FILE, 'w') as f:
        json.dump(st.session_state.timeline_events, f, indent=2)

def save_timeline_photo(event_key, photo_data, file_extension):
    """Save timeline photo to disk"""
    photo_file = PHOTOS_DIR / f"{event_key}{file_extension}"
    with open(photo_file, 'wb') as f:
        f.write(photo_data)

def delete_timeline_photo(event_key):
    """Delete timeline photo from disk"""
    # Try common image extensions
    for ext in ['.jpg', '.jpeg', '.png', '.gif']:
        photo_file = PHOTOS_DIR / f"{event_key}{ext}"
        if photo_file.exists():
            photo_file.unlink()
            break

# Custom CSS - Retro Macintosh Minimalistic Style
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #000;
        font-family: 'Monaco', 'Courier New', monospace;
        letter-spacing: 0.5px;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #000;
        font-family: 'Monaco', 'Courier New', monospace;
        border-bottom: 2px solid #000;
        padding-bottom: 0.5rem;
    }
    .project-card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 0px;
        margin-bottom: 1rem;
        border: 2px solid #000;
        font-size: 0.9rem;
        font-family: 'Monaco', 'Courier New', monospace;
    }
    .project-card h3 {
        font-family: 'Monaco', 'Courier New', monospace;
        margin: 0.5rem 0;
    }
    .project-card h4 {
        font-family: 'Monaco', 'Courier New', monospace;
        margin: 0.5rem 0;
    }
    .project-card p {
        font-family: 'Monaco', 'Courier New', monospace;
        margin: 0.3rem 0;
    }
    .timeline-item {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 0px;
        margin-bottom: 1rem;
        border: 2px solid #000;
        font-size: 0.9rem;
        font-family: 'Monaco', 'Courier New', monospace;
    }
    .timeline-item h4 {
        font-family: 'Monaco', 'Courier New', monospace;
        margin: 0.5rem 0;
    }
    .timeline-item p {
        font-family: 'Monaco', 'Courier New', monospace;
        margin: 0.3rem 0;
    }
    .timeline-date {
        font-weight: bold;
        color: #000;
        font-size: 0.85rem;
        font-family: 'Monaco', 'Courier New', monospace;
    }
    button {
        background-color: #f0f0f0;
        border: 2px solid #000;
        padding: 0.4rem 0.8rem;
        font-family: 'Monaco', 'Courier New', monospace;
        font-size: 0.85rem;
        cursor: pointer;
    }
    button:hover {
        background-color: #e0e0e0;
    }
    input, textarea, select {
        background-color: #fff;
        border: 2px solid #000;
        padding: 0.4rem;
        font-family: 'Monaco', 'Courier New', monospace;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">🚀 My Portfolio</div>', unsafe_allow_html=True)

# About section
st.markdown('<div class="section-header">👋 About Me</div>', unsafe_allow_html=True)
st.write("""
Hello! I'm **Isaac Ng**, a passionate learning enthusiast with a strong interest in **Machine Learning and Deep Learning**.
I love exploring innovative solutions and documenting my learning journey.
This portfolio showcases my milestone projects, fundamental experiments, and my learning timeline with visual memories.
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
            save_milestone_projects()
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
            save_small_projects()
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
        uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png", "gif"], key="timeline_photo")
        submitted = st.form_submit_button("Add Event", key="timeline_submit")

        if submitted and title:
            new_event = {
                "date": date.strftime('%Y-%m-%d'),
                "title": title,
                "description": description
            }
            st.session_state.timeline_events.append(new_event)
            save_timeline_events()
            
            # Store photo if uploaded
            if uploaded_file:
                event_key = f"{date.strftime('%Y-%m-%d')}_{title}"
                file_ext = Path(uploaded_file.name).suffix
                photo_data = uploaded_file.getvalue()
                st.session_state.timeline_photos[event_key] = photo_data
                save_timeline_photo(event_key, photo_data, file_ext)
            
            st.success("Event added successfully!")

# Display timeline events (sorted by date, most recent first)
if st.session_state.timeline_events:
    # Sort events by date
    sorted_events = sorted(st.session_state.timeline_events, key=lambda x: x['date'], reverse=True)
    for idx, event in enumerate(sorted_events):
        date_obj = datetime.strptime(event['date'], '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %Y')
        event_key = f"{event['date']}_{event['title']}"
        
        col1, col2, col3 = st.columns([1, 0.15, 0.15])
        
        with col1:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-date">{formatted_date}</div>
                <h4>{event['title']}</h4>
                <p>{event['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display photo if exists
            if event_key in st.session_state.timeline_photos:
                st.image(st.session_state.timeline_photos[event_key], use_column_width=True)
        
        with col2:
            if st.button("Edit", key=f"edit_{idx}"):
                st.session_state[f"editing_{idx}"] = True
        
        with col3:
            if st.button("Delete", key=f"delete_{idx}"):
                # Remove photo if exists
                if event_key in st.session_state.timeline_photos:
                    delete_timeline_photo(event_key)
                    del st.session_state.timeline_photos[event_key]
                st.session_state.timeline_events.pop(sorted_events.index(event))
                save_timeline_events()
                st.rerun()
        
        # Edit form
        if st.session_state.get(f"editing_{idx}", False):
            with st.form(f"edit_timeline_form_{idx}"):
                new_date = st.date_input("Event Date", value=datetime.strptime(event['date'], '%Y-%m-%d').date(), key=f"edit_date_{idx}")
                new_title = st.text_input("Event Title", value=event['title'], key=f"edit_title_{idx}")
                new_description = st.text_area("Event Description", value=event['description'], key=f"edit_desc_{idx}")
                new_photo = st.file_uploader("Update photo", type=["jpg", "jpeg", "png", "gif"], key=f"edit_photo_{idx}")
                
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
                        save_timeline_events()
                        
                        # Update photo
                        new_event_key = f"{new_date.strftime('%Y-%m-%d')}_{new_title}"
                        if new_photo:
                            file_ext = Path(new_photo.name).suffix
                            photo_data = new_photo.getvalue()
                            st.session_state.timeline_photos[new_event_key] = photo_data
                            save_timeline_photo(new_event_key, photo_data, file_ext)
                        elif event_key != new_event_key and event_key in st.session_state.timeline_photos:
                            # Rename photo key if date or title changed
                            photo_data = st.session_state.timeline_photos.pop(event_key)
                            # Delete old photo and save with new key
                            delete_timeline_photo(event_key)
                            for ext in ['.jpg', '.jpeg', '.png', '.gif']:
                                old_photo = PHOTOS_DIR / f"{event_key}{ext}"
                                if old_photo.exists():
                                    break
                            # Find extension of old photo
                            for ext in ['.jpg', '.jpeg', '.png', '.gif']:
                                old_photo = PHOTOS_DIR / f"{event_key}{ext}"
                                if old_photo.exists():
                                    photo_data = old_photo.read_bytes()
                                    delete_timeline_photo(event_key)
                                    save_timeline_photo(new_event_key, photo_data, ext)
                                    st.session_state.timeline_photos[new_event_key] = photo_data
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
    st.markdown("✉️ <span style='color: #666;'>Name:</span> Isaac Ng", unsafe_allow_html=True)
with col2:
    st.markdown("🖥️ <span style='color: #666;'>GitHub:</span> [Kgoing1](https://github.com/Kgoing1)", unsafe_allow_html=True)
with col3:
    st.markdown("🚀 <span style='color: #666;'>Focus:</span> ML/DL Learning", unsafe_allow_html=True)
