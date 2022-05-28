let openModels = document.querySelectorAll(".display-image");
let closer = document.querySelectorAll(".close");
let modal = document.querySelector(".modal");
let copyUrls = document.querySelectorAll(".copy-url");

for (image of openModels) {
  image.addEventListener("click", (e) => {
    e.target.nextElementSibling.style.display = "flex";
  });
}

if (closer) {
  for (let close of closer) {
    close.addEventListener("click", (e) => {
      e.target.parentElement.parentElement.style.display = "none";
    });
  }
}

for (shareLink of copyUrls) {
  shareLink.addEventListener("click", (e) => {
    toCopy =
      e.target.parentElement.previousElementSibling.firstElementChild
        .currentSrc;
    navigator.clipboard.writeText(toCopy);
    e.target.innerText = "Link Copied!";
  });
}
