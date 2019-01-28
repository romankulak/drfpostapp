import React from 'react';

export default class ErrorBoundary extends React.Component {
    static getDerivedStateFromError(error) {
        console.log(error);
        return { hasError: true };
    }

    constructor(props) {
        super(props);
        this.state = { hasError: false };
    }

    componentDidCatch(error, info) {
        console.error(error, info);
    }

    render() {
        const { hasError } = this.state;
        if (hasError) {
            return (
                <div>
                    <h1>
                        Something went wrong.
                    </h1>
                    <p>see console logs</p>
                </div>
            );
        }
        const { children } = this.props;
        return children;
    }
}
