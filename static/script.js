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


function AddFortune() {
  // A <form> element
  const FortuneInfo = document.querySelector("#AddFortuneForm");
  const formData = new FormData(FortuneInfo);
  const response = fetch("https://api.outworldindustries.com/addfortune/", {
    method: "POST",
    body: formData,
  });
  console.log(response.json());
}
