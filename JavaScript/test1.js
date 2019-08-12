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
  
var foo = 'Tom's bar';
var fetch=address.fullAddress();  
document.writeln(fetch);  
  
</script>  
