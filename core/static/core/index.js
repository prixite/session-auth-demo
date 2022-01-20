// const data = JSON.stringify({'username': 'admin', 'password': 'admin'});
const data = new URLSearchParams();
data.append('username', 'admin');
data.append('password', 'admin');

fetch("/api/login/", {
	method: "POST",
	body: data,
}).then((response) => console.log(response));
