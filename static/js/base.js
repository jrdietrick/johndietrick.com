document.addEventListener('DOMContentLoaded', function() {
    var overlay = document.getElementById('splash_overlay');
    if (overlay !== null) {
        overlay.onmouseover = function (event) {
            if (typeof(this.filters) == 'undefined') {
                this.style.opacity = 1.0;
            } else {
                this.filters.alpha.opacity = 80;
            }
        }
        overlay.onmouseout = function(event) {
            if (typeof(this.filters) == 'undefined') {
                this.style.opacity = 0.0;
            } else {
                this.filters.alpha.opacity = 0;
            }
        }
    }
});