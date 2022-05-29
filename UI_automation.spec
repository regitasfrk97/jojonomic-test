describe('Locate Number Plate', () => {
  it('Locate Number Plate', () => {
	const locate = 'Sydney 2000'
    
    cy.visit('https://www.service.nsw.gov.au/')
    cy.get('.form__text, .from--large').type('Apply for a number plate')
    cy.contains('submit').click()

    cy.wait()
    cy.contains('Find Location').click()
    cy.get('#locatorTextSearch').type(locate)
    cy.contains('submit').click()
    cy.get('#locatorListView').should('contain', 'Marrickville Service Centre')
  })
})