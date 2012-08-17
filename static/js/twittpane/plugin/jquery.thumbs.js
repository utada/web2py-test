(function($){
  $.fn.thumbs = function() {

    return this.each(function(i) {
      if (this.expanded_url === null) {
        console.log(this);
        return true;
      }
      var path = this.expanded_url.split('/');

      // twitpic.com
      if (path[2] === "twitpic.com") {
        this.thumbnail_url = "http://twitpic.com/show/thumb/"+path[3];
      }

      // yfrog.com
      if (path[2] === "yfrog.com") {
        this.thumbnail_url = "http://yfrog.com/"+path[3]+".th.jpg";
      }

      if (this.media_url !== undefined) {
        path = this.media_url.split('/');

        // pic.twitter.com
        if (path[2] === "p.twimg.com") {
          this.thumbnail_url = "http://p.twimg.com/"+path[3]+":thumb";
        }
      }
    });
  };
})(jQuery);
