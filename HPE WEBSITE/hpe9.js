const usageInput = document.getElementById('usage');
const voltageInput = document.getElementById('voltage');
const priceInput = document.getElementById('price');
const estimatedBillEl = document.getElementById('estimatedBill');
const voltageInfoEl = document.getElementById('voltageInfo');

function updateEstimate() {
  const usage = parseFloat(usageInput.value) || 0;
  const voltage = parseFloat(voltageInput.value) || 0;
  const price = parseFloat(priceInput.value) || 0;
  estimatedBillEl.textContent = `$${(usage * price).toFixed(2)}`;
  voltageInfoEl.textContent = `Voltage supplied: ${voltage}V`;
}

[usageInput, voltageInput, priceInput].forEach((input) => {
  input.addEventListener('input', updateEstimate);
});

updateEstimate();
