// like.js
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.like-btn').forEach((button) => {
    button.addEventListener('click', () => {
      const postId = button.dataset.postId
      const likeCountSpan = document.getElementById(`like-count-${postId}`)

      fetch(`/toggle_like/${postId}`, {
        method: 'GET',
        headers: {
          'X-CSRFToken': getCookie('csrftoken') // if you need CSRF
        }
      })
        .then((response) => response.json())
        .then((result) => {
          const icon = button.querySelector('i')
          if (result.liked) {
            icon.classList.remove('fa-regular', 'text-muted')
            icon.classList.add('fa-solid', 'fa-heart', 'text-danger')
          } else {
            icon.classList.remove('fa-solid', 'fa-heart', 'text-danger')
            icon.classList.add('fa-regular', 'fa-heart', 'text-muted')
          }
          likeCountSpan.textContent = result.like_count
        })
    })
  })
})

// Helper function for CSRF token
function getCookie(name) {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop().split(';').shift()
}
