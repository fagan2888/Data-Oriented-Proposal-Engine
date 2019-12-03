function calc()
{
  if (document.getElementById('autofill').checked) 
  {
      document.getElementById('contractType').value = Math.floor((Math.random() * 999999) + 1);
  }
}