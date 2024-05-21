document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Here you would typically send the login data to the server
    console.log('Username:', username);
    console.log('Password:', password);
    
    alert('Login successful!');
});
