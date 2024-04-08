const slider = () => {
  console.log("ddd");
  const slide = document.querySelectorAll(".news-item"),
    btn = document.querySelectorAll(".news-btn"),
    slider = document.querySelector(".news-content"),
    ul = document.querySelector(".news-dots");
  let currentSlide = 0,
    interval;

  //добавление точек на слайдер
  const renderDot = () => {
    for (let i = 0; i < slide.length; i++) {
      const li = document.createElement("li");
      li.classList.add("dot");
      ul.appendChild(li);
    }
  };
  renderDot();
  const dot = document.querySelectorAll(".dot");

  const prevSlide = (elem, index, strClass) => {
    elem[index].classList.remove(strClass);
  };

  const nextSlide = (elem, index, strClass) => {
    elem[index].classList.add(strClass);
  };

  const autoPlaySlide = () => {
    prevSlide(slide, currentSlide, "news-item-active");
    prevSlide(dot, currentSlide, "dot-active");
    currentSlide++;
    if (currentSlide >= slide.length) {
      currentSlide = 0;
    }
    nextSlide(slide, currentSlide, "news-item-active");
    nextSlide(dot, currentSlide, "dot-active");
  };

  const startSlide = (time = 3000) => {
    interval = setInterval(autoPlaySlide, time);
  };

  const stopSlide = () => {
    clearInterval(interval);
  };

  slider.addEventListener("click", (event) => {
    event.preventDefault();

    const target = event.target;
    if (!target.matches(".news-btn, .dot")) {
      return;
    }

    prevSlide(slide, currentSlide, "news-item-active");
    prevSlide(dot, currentSlide, "dot-active");

    if (target.matches("#arrow-right")) {
      currentSlide++;
    } else if (target.matches("#arrow-left")) {
      currentSlide--;
    } else if (target.matches(".dot")) {
      dot.forEach((elem, index) => {
        if (elem === target) {
          currentSlide = index;
        }
      });
    }

    if (currentSlide >= slide.length) {
      currentSlide = 0;
    }

    if (currentSlide < 0) {
      currentSlide = slide.length - 1;
    }
    nextSlide(slide, currentSlide, "news-item-active");
    nextSlide(dot, currentSlide, "dot-active");
  });

  slider.addEventListener("mouseover", (event) => {
    if (event.target.matches(".news-btn") || event.target.matches(".dot")) {
      stopSlide();
    }
  });
  slider.addEventListener("mouseout", (event) => {
    if (event.target.matches(".news-btn") || event.target.matches(".dot")) {
      startSlide();
    }
  });
  startSlide(1500);
};

slider();
