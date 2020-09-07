const postBtn = document.querySelector(".post-btn");
const modalWrapper = document.querySelector(".modal-wrapper");
const modal = document.querySelector(".modal");
const postModalX = document.querySelector(".modal-header i");
const modalPostBtn = document.querySelector(".modal-header button");
const modalFooterPlus = document.querySelector(".modal-footer span");
const modalInput = document.querySelector(".modal-input");
const user = document.querySelector(".user");
const sidebar = document.querySelector(".sidebar");
const sidebarWrapper = document.querySelector(".sidebar-wrapper");
const xBtn = document.querySelector(".sidebar-header i");
// News feed page
// Post modal
postBtn.addEventListener("click", () => {
  modal.style.display = "block";
  modalWrapper.classList.add("modal-wrapper-display");
});

const changeOpacity = (x) => {
  modalPostBtn.style.opacity = x;
  modalFooterPlus.style.opacity = x;
};

postModalX.addEventListener("click", () => {
  modal.style.display = "none";
  modalWrapper.classList.remove("modal-wrapper-display");

  if (modalInput.value !== "") {
    modalInput.value = "";
    changeOpacity(0.5);
  }
});

modalInput.addEventListener("keypress", (e) => {
  if (e.target.value !== "") {
    changeOpacity(1);
  }
});

modalInput.addEventListener("blur", (e) => {
  if (e.target.value === "") {
    changeOpacity(0.5);
  }
});

// Sidebar
user.addEventListener("click", () => {
  sidebar.classList.add("sidebar-display");
  sidebarWrapper.classList.add("sidebar-wrapper-display");
});

xBtn.addEventListener("click", () => {
  sidebar.classList.remove("sidebar-display");
  sidebarWrapper.classList.remove("sidebar-wrapper-display");
});

// dark mode
const toggle = document.querySelector(".toggle");
const circle = document.querySelector(".circle");
const darkElements1 = document.querySelectorAll(".dark-mode-1");
const darkElements2 = document.querySelectorAll(".dark-mode-2");
const lighTexts = document.querySelectorAll(".light-text");
const borders = document.querySelectorAll(".border");

toggle.addEventListener("click", () => {
  circle.classList.toggle("move");
  Array.from(darkElements1).map((darkEl1) =>
    darkEl1.classList.toggle("dark-1")
  );
  Array.from(darkElements2).map((darkEl2) =>
    darkEl2.classList.toggle("dark-2")
  );
  Array.from(lighTexts).map((lighText) => lighText.classList.toggle("light"));
  Array.from(borders).map((border) => border.classList.toggle("border-color"));
});

const postTweet = document.getElementById("posttweet");

$posttweetta.keyup(function (e) {
  $totchars = $(this).val().length;
  if ($totchars <= 250) $totalchars.text($totchars);
  else {
    $totalchars.text("250");
    $(this).val($(this).val().substring(0, 250));
  }
});

$("#posttweetbut").click(function () {
  if (($taval = $.trim($posttweetta.val())).length > 0) {
    $tweetscontainer.prepend(tweetitem($taval));
    $posttweetta.val("");
    $statslistitemcount.text(parseInt($statslistitemcount.text()) + 1);
  }
});
