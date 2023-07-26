const button = $("#btn");
const videoArea = $("#video");
const titleArea = $("#title");
const contentArea = $("#content");
let number = 0;

function getData() {
    return new Promise(function(resolve, reject) {
      $.ajax('ajax.json', {
        success: function(data) {
          resolve(data);
        },
        error: function(error) {
          reject(error);
        }
      });
    });
  };

  function changeVideo() {
    button.click(function() {
      getData()
        .then(function(videoData) {
          videoArea.attr("src", videoData[number].url);
          titleArea.html(videoData[number].title);
          contentArea.html(videoData[number].content);
          number == 2 ? number = 0 : number++;
        })
        .catch(function(error) {
          console.error("Error fetching data:", error);
        });
    });
  };

changeVideo();


  