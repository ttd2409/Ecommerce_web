var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var acction = this.dataset.acction
        console.log('productId',productId,'acction',acction)
                // 'user:',user || 'string:', variable
        console.log('user:', user)
        // ktra user đăng nhập vào chưa
        if (user === 'AnonymousUser'){
            console.log('user not logged in')
        } else {
            // nếu login thì thông báo
            console.log('user logged in, success add')
        
        }
    })
}