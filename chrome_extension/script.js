var current_url = "https://edition.cnn.com/2023/03/20/world/ipcc-synthesis-report-climate-intl/index.html";
var azure_url = "http://localhost:7071/api/fake_news_deployment";
const usersName = JSON.stringify({ url: current_url });
customConfig = {
    headers: {
    'Content-Type': 'application/json'
    }
};
const result = await axios.post(azure_url,);

console.log(result.data.data); // '{"name":"John Doe"}'
console.log(result.data.headers['Content-Type']); // 'application/json',