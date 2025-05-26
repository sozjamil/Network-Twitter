# Social Network Platform

A full-featured social media web application built with Django that enables users to connect, share content, and interact with each other's posts.
and here is the demo: https://network-twitter-yaya.onrender.com/

## Technologies Used

### Backend
- **Python** (v3.9+)
- **Django** (v4.0+) - Web framework
- **Django ORM** - Database abstraction
- **SQLite** (Development) / **PostgreSQL** (Production-ready)

### Frontend
- **HTML5** - Page structure
- **CSS3** - Styling and layout
- **JavaScript (ES6+)** - Interactive elements
- **Bootstrap 5** - Responsive design components

### APIs
- **Fetch API** - For asynchronous operations
- **Django REST Framework** (Optional) - For API endpoints

## Core Features

### 1. User Authentication System
- Secure user registration with form validation
- Login/logout functionality with session management
- Protected routes for authenticated content
- User profile pages with activity metrics

### 2. Post Management System
- **New Post Creation**
  - Rich text area for content
  - Character limit validation
  - Instant post submission

- **Post Display**
  - Chronological feed (newest first)
  - Author attribution with profile links
  - Precise timestamp display
  - Like counter with visual feedback

- **Post Editing**
  - In-place content editing
  - Edit history tracking (optional)
  - Version comparison (optional)

### 3. Social Interaction Features
- **Following System**
  - Follow/unfollow toggle
  - Follower/following counts
  - Following-only content feed

- **Like System**
  - Single-click like/unlike
  - Real-time like counter updates
  - Liked post visual indication

### 4. Content Presentation
- **Pagination System**
  - 10 posts per page standard
  - Next/previous navigation
  - Page number indicators

- **Profile Pages**
  - User statistics dashboard
  - Complete post history
  - Follow relationship status

## Data Architecture

### Database Models
| Model       | Key Fields                          | Relationships               |
|-------------|-------------------------------------|-----------------------------|
| User        | username, email, password          | Self-referential (follows)  |
| Post        | content, timestamp, edited         | Many-to-one with User       |
| Like        | created_at                          | Many-to-one with User/Post  |
| Follow      | created_at                          | Many-to-many between Users  |

### API Endpoints
- `POST /post` - Create new post
- `PUT /post/<id>` - Edit existing post
- `POST /like/<post_id>` - Toggle like
- `POST /follow/<user_id>` - Toggle follow
- `GET /posts` - Paginated post feed
- `GET /profile/<username>` - User profile data

