<table border="0" cellspacing="3" cellpadding="4">
	<thead>
	</thead>
	<tr>
		<th colspan="4">Pharmacy Receipt</th>
	</tr>
	<tr>
		<td colspan="4"><center><H1>Clearance Receipt for payment to date</H1></center></td>
	</tr>
	<tr>
		<td colspan="4">Time: {$smarty.now|date_format:'d/m/Y H:i:s'}</td>
	</tr>
	<tr>
		<td colspan="1"><H3>Name:</H3></td>
		<td colspan="3"><H3>{$patient->name}</H3></td>
	</tr>
	<tr>
		<td colspan="1"><H3>Age:</H3></td>
		<td colspan="3"><H3>{$patient->age}</H3></td>
	</tr>
	<tr>
		<td colspan="4">
			<table>
				<thead>
					<tr>
						<th><u>Name</u></th>
						<th><u>Quantity</u></th>
						<th><u>Unit Price</u></th>
						<th><u>Date Added</u></th>
						<th><u>Subtotal</u></th>
					</tr>
				</thead>
				{foreach $patient_products as $patient_product}
					<tr>
						<td>{$patient_product->product->name}</td>
						<td>{$patient_product->quantity}</td>
						<td>{$patient_product->product->price}</td>
						<td>{$patient_product->time_changed|date_format:"d/m/Y"}</td>
						<td class="subtotal">{$patient_product->quantity * $patient_product->product->price}</td>
					</tr>
				{/foreach}
				<tr>
					<td></td>
					<td></td>
					<td></td>
					<td>Total:</td>
					<td class="total">{$total}</td>
				</tr>
			</table>
		</td>
	</tr>
</table>