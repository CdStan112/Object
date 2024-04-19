const slider2userprofile = () => {

    const main = document.querySelector('.mine-books-wrapper'),
        forButtons = document.querySelector('.mine-books-push-buttons'),
        wrap = document.querySelector('.mine-books-horiz'),
        slides = document.querySelector('.mine-books-horiz').children;
    let slidesToShow = 5,
        options = {
            position: 0,
            infinity: true,
            widthSlide: Math.floor(100 / slidesToShow),
        },
        responsive = [{
            breakpoint: 1024,
            slidesToShow: 3
        },
            {
                breakpoint: 768,
                slidesToShow: 2
            },
            {
                breakpoint: 576,
                slidesToShow: 1
            }
        ];


    let prev, next, prevnext;

    const init = () => {
        responseInit();
        addGloClass();
        //addArrowPrev();
        addStyle();
        addArrow();
        //addArrowNext();
        controlSlider();
    }

    const addGloClass = () => {
        main.classList.add('glo-slider');
        wrap.classList.add('glo-slider__wrap');
        for (const item of slides) {
            item.classList.add('glo-slider__item');
        }
    }
    const addStyle = () => {
        let style = document.getElementById('slider2-style');
        if (!style) {
            style = document.createElement('style');
            style.id = 'slider2-style';
        }
        style.textContent = `
        .glo-slider{
            overflow:hidden !important;

        }
        .glo-slider__wrap{
            display:flex !important;
            transition:transform 0.5s !important;
            will-change:transform !important;
            justify-content: space-between;
        }
        .glo-slider__item{
            display:flex !important;
            align-items:center;
            justify-content:center;
            margin: auto 0 !important; 
        }
        `;
        document.head.appendChild(style);
    }

    const controlSlider = () => {
        prev.addEventListener('click', prevSlider.bind(this));
        next.addEventListener('click', nextSlider.bind(this));
    }

    const prevSlider = () => {
        if (options.infinity || options.position > 0) {
            --options.position;
            if (options.position < 0) {
                options.position = slides.length - slidesToShow;
            }
            wrap.style.transform = `translateX(-${options.position * options.widthSlide}%)`;
        }
    }

    const nextSlider = () => {
        if (options.infinity || options.position < slides.length - slidesToShow) {
            ++options.position;
            if (options.position > slides.length - slidesToShow) {
                options.position = 0;
            }
            wrap.style.transform = `translateX(-${options.position * options.widthSlide}%)`;
        }
    }


    const addArrow = () => {


        prev = document.createElement('button');
        prev.style.cssText = ''
        prev.className = 'glo-slider__prev';
        forButtons.appendChild(prev)

        const svgAddLeft = `<svg viewBox="0 0 960 960" height="60" width="60">
                    <use xlink:href="../static/img/sprite.svg#icon-service-arrow-left"></use>
                </svg>`
        prev.innerHTML = svgAddLeft;

        next = document.createElement('button');

        next.className = 'glo-slider__next';
        forButtons.appendChild(next)
        const svgAddRight = `<svg viewBox="0 0 960 960" height="60" width="60">
                    <use xlink:href="../static/img/sprite.svg#icon-service-arrow-right"></use>
                </svg>`
        next.innerHTML = svgAddRight;
    }
    /*
    const addArrowPrev = () => {
        prev = document.createElement('button' );
        prev.style.cssText='position: absolute;'

        prev.className = 'glo-slider__prev';
        //main.appendChild(prev);
        main.insertBefore(prev,wrap);

        const svgAddLeft = `<a><svg viewBox="0 0 960 960" height="24" width="24">
                    <use xlink:href="../static/img/sprite.svg#icon-service-arrow-left"></use>
                </svg></a>`
        prev.innerHTML = svgAddLeft;


    }

    const addArrowNext = () => {
        next = document.createElement('button');
        next.className = 'glo-slider__next';

        main.appendChild(next);
           const svgAddRight = `<svg viewBox="0 0 960 960" height="24" width="24">
                    <use xlink:href="../static/img/sprite.svg#icon-service-arrow-right"></use>
                </svg>`
        next.innerHTML = svgAddRight;
    }

*/


    const responseInit = () => {
        const slidesToShowDefault = slidesToShow;
        const allRespone = responsive.map(item => item.breakpoint);
        const maxResponse = Math.max(...allRespone);

        const checkResponse = () => {
            const widthWindow = document.documentElement.clientWidth;
            if (widthWindow < maxResponse) {
                for (let i = 0; i < allRespone.length; i++) {
                    if (widthWindow < allRespone[i]) {
                        slidesToShow = responsive[i].slidesToShow;
                        options.widthSlide = Math.floor(100 / slidesToShow);
                        addStyle();
                    }
                }
            } else {
                slidesToShow = slidesToShowDefault;
                options.widthSlide = Math.floor(100 / slidesToShow);
                addStyle();
            }
        };
        checkResponse();
        window.addEventListener('resize', checkResponse);

    }

    init();
}
slider2userprofile();

