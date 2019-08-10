<script>  
function round(n, upperBound, lowerBound){
  if(n > upperBound) || (n < lowerBound){
    throw 'Number ' + String(n) + ' is more than ' + String(upperBound) + ' or less than ' + String(lowerBound);
  }else if(n < ((upperBound + lowerBound)/2)){
    return lowerBound;
  }else{
    return upperBound;
  }
} // SyntaxError: expected expression, got '||'
  
</script>  
