// Wait for the DOM to finish loading
document.addEventListener("DOMContentLoaded", function () {
  // Get the current tab URL
  chrome.tabs.query(
    { active: true, currentWindow: true },
    async function (tabs) {
      var azure_url = "http://localhost:7071/api/fake_news_deployment";

      var current_url = tabs[0].url;
      document.getElementById("url").value = current_url;
      var makeRequest = function () {
        fetch(azure_url, {
          method: "POST",
          mode: "no-cors",
          headers: {
            Accept: "application.json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
          body: JSON.stringify([{ url: current_url }]),
        })
          .then((response) => {
            return response.json(); // << This is the problem
          })
          .then((responseData) => {
            // responseData = undefined
            console.log(data);
          })
          .catch(function (err) {
            console.log(err);
          });
      };
      makeRequest();
    }
  );
});
//let response = fetch(azure_url, {
//      method: "POST",
//      mode: "no-cors",
//      headers: {
//        Accept: "application/json",
//        "Content-Type": "application/json;",
//      },
//      body: JSON.stringify([{ url: current_url }]),
//    })
//    .then((response) => response.json())
//    .then(console.log(response));
