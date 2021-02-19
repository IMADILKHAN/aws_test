var Data = []
fetch('http://127.0.0.1:8081/memes')
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                appendData(data);

            })
            .catch(function (err) {
                console.log('error: ');
            });
        function appendData(Data) {
            var mainContainer = document.getElementById("myData");
            for (var i = 0; i < Math.max(100,Data.length); i++) {
                var div = document.createElement("div");
                var label = document.createElement('h6')
                var label2 = document.createElement('h6')
                var img = document.createElement('img')
                label.innerHTML = Data[i]['name']
                label2.innerHTML = Data[i]['caption']
                img.src = Data[i]['url']
                // div.innerHTML = 'Name: ' + Data[i]['name'];
                div.appendChild(label)
                div.appendChild(label2)
                div.appendChild(img)
                mainContainer.appendChild(div);
            }
        }

function sendJSON(){

                    let name = document.querySelector('#name');
                    let caption = document.querySelector('#caption');
                    let urls = document.querySelector('#url');

                    // Creating a XHR object
                    let xhr = new XMLHttpRequest();
                    let url = "http://127.0.0.1:8081/memes";

                    // open a connection
                    xhr.open("POST", url, true);

                    // Set the request header i.e. which type of content you are sending
                    xhr.setRequestHeader("Content-Type", "application/json");

                    // Create a state change callback
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState === 4 && xhr.status === 200) {


                        }
                    };

                    // Converting JSON data to string
                    var data = JSON.stringify({ "name": name.value, "caption": caption.value ,"url":urls.value});

                    // Sending data with the request
                    xhr.send(data);
                    location.reload()
                }
