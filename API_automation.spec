describe('Test Weheartit', () => {
	it('Current Weather - GET', () => {
	    cy.request('GET', '/current?lat=${lat}&lon=${lon}').as('currentGet');
	    cy.get('@currentGet').then(current => {
	        expect(current.status).to.eq(200);
	    });
	});

	it('Forecast Hourly - GET', () => {
	    cy.request('GET', '/forecast/3hourly?postal_code=${postal_code}').as('forecastGet');
	    cy.get('@forecastGet').then(forecast => {
	        expect(forecast.status).to.eq(200);
	    });
	});
});