def main():
    """Sample Python script to test MCP GitHub integration."""
    print('Hello from MCP!')
    
    # Sample data processing
    data = [
        {'id': 1, 'value': 'test1'},
        {'id': 2, 'value': 'test2'},
        {'id': 3, 'value': 'test3'}
    ]
    
    for item in data:
        process_item(item)
        
def process_item(item):
    """Process a single data item."""
    print(f'Processing item {item["id"]}: {item["value"]}')

if __name__ == '__main__':
    main()