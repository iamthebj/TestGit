<script>  
var address=  
{  
company:"Javatpoint",  
city:"Noida",  
state:"UP",  
fullAddress:function()  
{  
return this.cothis.city"+this.state;  
}  
};
var fetch=address.fullAddress();  
document.writeln(fetch);  
  
</script>  
