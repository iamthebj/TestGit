<script>  
var address=  
{  
company:"Javatpoint",  
city:"Noida",  
state:"UP",  
fullAddress:function()  
{  
return this.company+" "+this.city+" "+this.state;  
}  
};    
var fetch=address.fullAddress();  
document.wri(fetch);  
</script>  
