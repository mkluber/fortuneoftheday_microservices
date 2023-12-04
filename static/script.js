function myFunction() {
    console.log('Hello world!');
  }
  
myFunction();

function ScanFortune() {
  const url = 'https://api.outworldindustries.com/scanfortune/';
  fetch(url)
    .then(response => response.json())
    .then(json => {
      console.log(json);
      document.getElementById("ScanFortuneOutput").innerHTML = JSON.stringify(json);
    });
}