let openModels = document.querySelectorAll(".display-image");
let closer = document.querySelectorAll(".close");
let modal = document.querySelector(".modal");
let copyUrls = document.querySelectorAll(".copy-url");
let displayAll = document.querySelector(".all-photos");
let locationSelection = document.querySelectorAll(".nav");
let allSections = document.querySelectorAll(".photos");

for (selector of locationSelection) {
  selector.addEventListener("click", (e) => {
    for (section of allSections) {
      section.classList.remove("active-section");
    }
    for (selector of locationSelection) {
      selector.classList.remove("active");
    }
    e.target.classList.add("active");
    for (section of allSections) {
      if (section.id == e.target.innerText.toLowerCase()) {
        section.classList.add("active-section");
      }
    }
  });
}

displayAll.addEventListener("click", (e) => {
  for (section of allSections) {
    section.classList.remove("active-section");
  }
  for (selector of locationSelection) {
    selector.classList.remove("active");
  }
  for (section of allSections) {
    if (section.id == e.target.className) {
      section.classList.add("active-section");
    }
  }
});

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
