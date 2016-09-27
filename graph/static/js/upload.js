var getBlobURL=(window.URL&& URL.createObjectURL.bind(URL))||window.createObjectURL||(window.webkitURL&&webkitURL.revokeObjectURL.bind(webkitURL));
var revokeBlobURL=(window.URL&&URL.revokeObjectURL.bind(URL))||(window.webkitURL&&webkitURL.revokeObjectURL.bind(webkitURL))||window.revokeBlobURL;

window.onload=function () {
		 $('#id_username').attr('placeholder','UserName');
		 $('#id_C_lass').attr('placeholder','Class');
			$('#id_username').maxLength(4);
			$('#id_C_lass').maxLength(3);
			

		var id_headImg=document.getElementById('id_headImg');
		var Atlas=document.getElementsByClassName('Atlas')[0];

		$('.user_list>form>input').focus(function () {
			$(this).addClass('holder');
		});
		$('.user_list>form>input').blur(function () {
			$(this).removeClass('holder');
		});

		id_headImg.onchange=function (e) {
			var files=this.files;
			var type=files[0].type;
			if (type.substring(0,6) !=="image/") {
				alert("ooo");
				return false;
			};
			var img=document.createElement('img');
			img.src=getBlobURL(files[0]);
			$('.Atlas>img').replaceWith(
				img.onload=function () {
					this.width=120;
					Atlas.appendChild(this);
					revokeBlobURL(this.src);
					return false;
			});
			if ($('.Atlas>img')) $('.btn_a').animate({opacity:0},0);
			else $('.btn_a').animate({opacity:1},0);

		};



};


jQuery.fn.maxLength = function(max){
        this.each(function(){
            var type = this.tagName.toLowerCase();
            var inputType = this.type? this.type.toLowerCase() : null;
            if(type == "input" && inputType == "text" || inputType == "password"){
                this.maxLength = max;
            }
            else if(type == "textarea"){
                this.onkeypress = function(e){
                    var ob = e || event;
                    var keyCode = ob.keyCode;
                    var hasSelection = document.selection? document.selection.createRange().text.length > 0 : this.selectionStart != this.selectionEnd;
                    return !(this.value.length >= max && (keyCode > 50 || keyCode == 32 || keyCode == 0 || keyCode == 13) && !ob.ctrlKey && !ob.altKey && !hasSelection);
                };
                this.onkeyup = function(){
                    if(this.value.length > max){
                        this.value = this.value.substring(0,max);
                    }
                };
            }
        })
}