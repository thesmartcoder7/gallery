let openModels = document.querySelectorAll(".display-image") as NodeListOf<HTMLImageElement>;
let closer = document.querySelectorAll(".close")as NodeListOf<HTMLParagraphElement>; 
let modal = document.querySelector(".modal") as HTMLDivElement;
let copyUrls = document.querySelectorAll(".copy-url") as NodeListOf<HTMLParagraphElement>;
let displayAll = document.querySelector(".all-photos") as HTMLParagraphElement; 
let locationSelection = document.querySelectorAll(".nav") as NodeListOf<HTMLUListElement>;
let allSections = document.querySelectorAll(".photos") as NodeListOf<HTMLDivElement>;

if (locationSelection) {
  for (let selector of locationSelection) {
    selector.addEventListener("click", (e: any) => {
      for (let section of allSections) {
        section.classList.remove("active-section");
      }
      for (selector of locationSelection) {
        selector.classList.remove("active");
      }
      e.target.classList.add("active");
      for (let section of allSections) {
        if (section.id == e.target.innerText.toLowerCase()) {
          section.classList.add("active-section");
        }
      }
    });
  }
}

if (displayAll) {
  displayAll.addEventListener("click", (e: any) => {
    for (let section of allSections) {
      section.classList.remove("active-section");
    }
    for (let selector of locationSelection) {
      selector.classList.remove("active");
    }
    for (let section of allSections) {
      if (section.id == e.target.className) {
        section.classList.add("active-section");
      }
    }
  });
}

if (openModels) {
  for (let image of openModels) {
    image.addEventListener("click", (e: any) => {
      e.target.nextElementSibling.style.display = "flex";
    });
  }
}

if (closer) {
  for (let close of closer) {
    close.addEventListener("click", (e: any) => {
      e.target.parentElement.parentElement.style.display = "none";
    });
  }
}

if (copyUrls) {
  for (let shareLink of copyUrls) {
    shareLink.addEventListener("click", (e: any) => {
      let toCopy =
        e.target.parentElement.previousElementSibling.firstElementChild
          .currentSrc;
      navigator.clipboard.writeText(toCopy);
      e.target.innerText = "Link Copied!";
    });
  }
}
