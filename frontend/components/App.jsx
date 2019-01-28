import React from 'react';
import ErrorBoundary from 'error';
import { csrfToken } from 'helpers';


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: {
                results: []
            },
            searchQuery: ''
        };
        this.fetchData = this.fetchData.bind(this);
        this.handleRequest = this.handleRequest.bind(this);
        this.setStateFromJson = this.setStateFromJson.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }

    componentWillMount() {
        this.fetchData();
    }

    setStateFromJson(json) {
        const graphData = json ? { data: json } : {};
        this.setState(Object.assign(graphData));
    }

    fetchData() {
        const requestData = {
            url: '/api/v1/posts',
            method: 'GET',
            formElData: {}
        };
        this.handleRequest(requestData);
    }

    handleRequest(requestData) {
        const { url, method, formElData } = requestData;
        const formData = new FormData();
        for (const prop in formElData) {
            if (formElData.hasOwnProperty(prop)) {
                formData.append(prop, formElData[prop]);
            }
        }
        fetch(url, {
            method,
            credentials: 'same-origin',
            headers: { 'X-CSRFToken': csrfToken() },
            body: method === 'POST' ? formData : null
        }).then((response) => {
            if (response.ok) return response.json();

            console.error(response.status, response.statusText);
            return null;
        }).then(json => this.setStateFromJson(json));
    }

    handleSearch(e) {
        const searchQuery = e.target.value.toLowerCase();
        this.setState({ searchQuery });
    }

    render() {
        const { data } = this.state;
        const filteredPosts = data.results.filter(
            p => (
                p.title.toLowerCase().indexOf(this.state.searchQuery) !== -1
                || p.content.toLowerCase().indexOf(this.state.searchQuery) !== -1
                || p.owner.toLowerCase().indexOf(this.state.searchQuery) !== -1
            )
        );
        return (
            <div>
                <ErrorBoundary>
                    <input
                      placeholder="Search"
                      type="text"
                      onChange={this.handleSearch}
                    />
                    <ul>
                        {
                            filteredPosts.map(post => (
                                <li key={post.id}>
                                    <h3 className="title">{post.title} </h3>
                                    <p className="content">{post.content} </p>
                                    created: {post.created} <br />
                                    author: {post.owner} <br />
                                    {post.likes} likes
                                </li>
                            ))
                        }
                    </ul>
                </ErrorBoundary>
            </div>
        );
    }
}
