import React, { Component, Fragment } from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'
import { Card, CardBody, CardTitle, CardText, Container } from 'reactstrap'

import { Loading } from '../utils'

class MyTeams extends Component {

    render() {
        const { data: { loading, myTeams } } = this.props
        return (
            <Container>
                <h1>My Teams</h1>
                {loading ? <Loading /> : (
                    <Fragment>
                        {myTeams.map(team => (
                            <Card key={`team-${team.id}`} style={{ marginTop: '2rem' }}>
                                <CardBody>
                                    <CardTitle>{team.name}</CardTitle>
                                    <CardText>
                                        {team.players.map(p => p.username).join(', ')}
                                    </CardText>
                                </CardBody>
                            </Card>
                        ))}
                    </Fragment>
                )}
            </Container>
        )
    }
}

const query = gql`
    query {
        myTeams {
            id
            name
            captain {
                id
                username
            }
            players {
                id
                username
            }
        }
    }
`

MyTeams = graphql(query)(MyTeams)

export default MyTeams
