export function loadTweets(callback) {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const response = "json";
  const url = "http://localhost:8000/api/tweets/";

  xhr.responseType = response;
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = (e) => {
    console.log(e);
    callback({ message: "There was an error fetching the data..." }, 400);
  };
  xhr.send();
}
