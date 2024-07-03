
// // Attach a click event listener to the follow/unfollow button
// document.addEventListener('DOMContentLoaded', () => {
//     const followBtn = document.getElementById('follow-btn');
//     const unfollowBtn = document.getElementById('unfollow-btn');

//     if (followBtn) {
//         followBtn.addEventListener('click', toggleFollow);
//     }

//     if (unfollowBtn) {
//         unfollowBtn.addEventListener('click', toggleFollow);
//     }
// });

// // Function to handle the follow/unfollow action
// function toggleFollow() {
//     const user_id = this.dataset.userId;
//     const action = this.dataset.action;

//     // Send a POST request to the follow_unfollow URL
//     fetch('/follow_unfollow/', {
//         method: 'POST',
//         body: JSON.stringify({
//             user_id: user_id,
//             action: action
//         }),
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCookie('csrftoken')
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle the response (update button text, UI, etc.)
//         console.log(data);

//         // Update the button's text based on the response from the server
//         if (data.status === 'success') {
//             if (action === 'follow') {
//                 document.getElementById('follow-btn').innerText = 'Unfollow';
//             } else if (action === 'unfollow') {
//                 document.getElementById('follow-btn').innerText = 'Follow';
//             }
//         }
//     })
//     .catch(error => console.log(error));
// }

// // Helper function to get the value of the CSRF token
// function getCookie(name) {
//     const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
//     return cookieValue ? cookieValue.pop() : '';
// }